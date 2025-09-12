from round_tax_amount_row_wise.override.override_doctype_class_having_accounts_controller import (
	get_override_doctype_class,
)

try:
	override_doctype_class = get_override_doctype_class()
except Exception:
	pass
