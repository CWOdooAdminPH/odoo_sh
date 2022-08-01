# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2022 Openfellas (http://openfellas.com) All Rights Reserved.
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsibility of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# guarantees and support are strongly advised to contact support@openfellas.com
#
##############################################################################

from odoo import api, fields, models
from odoo.tools import is_html_empty


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    header_html = fields.Html(
        string='Header HTML',
    )

    @api.model
    def default_get(self, fields_list):
        default_vals = super().default_get(fields_list)

        if (
            'header_html' in fields_list and
            default_vals.get('sale_order_template_id', False) and
            not default_vals.get('header_html', False)
        ):
            template = self.env['sale.order.template'].browse(
                default_vals.get('sale_order_template_id')
            ).with_context(
                lang=self.env['res.partner'].browse(
                    default_vals.get('partner_id')
                ).lang or self.env.user.lang
            )

            if not is_html_empty(template.header_html):
                default_vals['header_html'] = template.header_html

        return default_vals

    @api.onchange('sale_order_template_id')
    def onchange_sale_order_template_id(self):
        super().onchange_sale_order_template_id()

        if not self.sale_order_template_id:
            return

        template = self.sale_order_template_id.with_context(
            lang=self.partner_id.lang
        )

        if not is_html_empty(template.header_html):
            self.header_html = template.header_html

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        super(SaleOrder, self).onchange_partner_id()

        template = self.sale_order_template_id.with_context(
            lang=self.partner_id.lang
        )
        if not is_html_empty(template.header_html):
            self.header_html = template.header_html
