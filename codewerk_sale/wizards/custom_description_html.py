# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Openfellas (http://openfellas.com) All Rights Reserved.
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsibility of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# guarantees and support are strongly advised to contact support@openfellas.com
#

from odoo import fields, models


class WizardCustomDescriptionHtml(models.TransientModel):
    _name = 'wizard.sol.description.html'
    _description = 'SOL Description HTML'

    product_id = fields.Many2one(
        comodel_name='product.product',
        readonly=True,
    )
    description_html = fields.Html(
        string='Description HTML'
    )

    def action_update_description_field(self):
        line = self.env['sale.order.line'].browse(
            self.env.context['active_ids']
        )
        line.description_html = self.description_html
