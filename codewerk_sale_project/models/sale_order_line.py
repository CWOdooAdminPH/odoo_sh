from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _timesheet_create_project_prepare_values(self):
        vals = super()._timesheet_create_project_prepare_values()

        if self.order_id.project_name:
            vals.update({
                'name': self.order_id.project_name
            })

        return vals
