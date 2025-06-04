from round_tax_amount_row_wise.override.taxes_and_totals import (
	calculate_taxes_and_totals as calculate_taxes_and_totals_class,
)


class CustomAccountControllers:
	def calculate_taxes_and_totals(self):
		calculate_taxes_and_totals_class(self)

		if self.doctype in ("Sales Order", "Delivery Note", "Sales Invoice", "POS Invoice",):
			self.calculate_commission()
			self.calculate_contribution()
