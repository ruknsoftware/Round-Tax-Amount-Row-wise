import sys

import frappe
from erpnext.controllers.accounts_controller import AccountsController
from frappe.installer import update_site_config
from frappe.modules.import_file import get_controller

from round_tax_amount_row_wise.override.taxes_and_totals import (
	calculate_taxes_and_totals as calculate_taxes_and_totals_class,
)


class CustomAccountControllers:
	def calculate_taxes_and_totals(self):
		calculate_taxes_and_totals_class(self)

		if self.doctype in ("Sales Order", "Delivery Note", "Sales Invoice", "POS Invoice",):
			self.calculate_commission()
			self.calculate_contribution()


def get_override_doctype_class_name(doctype):
	return f"Custom{doctype.replace(' ', '')}"


def set_override_doctype_class():
	doctypes = frappe.get_all(
		"DocType", filters={"istable": 0, "issingle": 0, "is_virtual": 0}, pluck="name"
	)

	override_doctype_class = {}
	original_doctype_class = {}

	for doctype in doctypes:
		try:
			doctype_class = get_controller(doctype)
		except ImportError:
			continue

		if issubclass(doctype_class, AccountsController):
			override_class_name = get_override_doctype_class_name(doctype)
			override_doctype_class[doctype] = (
				f"{sys.modules[__name__].__name__}.{override_class_name}"
			)
			original_doctype_class[doctype] = (
				f"{doctype_class.__module__}.{doctype_class.__name__}"
			)
	update_site_config("override_doctype_class", override_doctype_class)
	update_site_config("original_doctype_class", original_doctype_class)
	return override_doctype_class


def get_override_doctype_class():
	override_doctype_class = frappe.get_site_config().get("override_doctype_class")
	original_doctype_class = frappe.get_site_config().get("original_doctype_class")
	if not override_doctype_class:
		override_doctype_class = set_override_doctype_class()
		original_doctype_class = frappe.get_site_config().get("original_doctype_class")

	for doctype in override_doctype_class.keys():
		doctype_class_path = original_doctype_class[doctype]
		doctype_class = frappe.get_attr(doctype_class_path)
		override_class_name = get_override_doctype_class_name(doctype)
		if not hasattr(sys.modules[__name__], override_class_name):
			override_class = type(
				override_class_name, (CustomAccountControllers, doctype_class), {}
			)
			setattr(sys.modules[__name__], override_class_name, override_class)

	return override_doctype_class

	def __getattr__(name):
		"""
		Dynamically create and return a custom override class when accessed.
		If the class already exists, return it instead of creating a new one.
		"""
		# Check if class is already defined in the module (important for repeated access)
		mod = sys.modules[__name__]
		if hasattr(mod, name):
			return getattr(mod, name)

		if name.startswith("Custom"):
			get_override_doctype_class()
			if hasattr(mod, name):
				return getattr(mod, name)
		# If the class does not exist, raise an AttributeError
		raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
