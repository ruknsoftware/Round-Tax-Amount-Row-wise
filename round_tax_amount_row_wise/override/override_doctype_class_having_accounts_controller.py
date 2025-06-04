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

	for doctype in doctypes:
		try:
			doctype_class = get_controller(doctype)
		except ImportError:
			continue

		if issubclass(doctype_class, AccountsController):
			override_class_name = get_override_doctype_class_name(doctype)
			override_doctype_class[
				doctype
			] = f"round_tax_amount_row_wise.override.override_doctype_class_having_accounts_controller.{override_class_name}"

	update_site_config("override_doctype_class", override_doctype_class)
	return override_doctype_class
