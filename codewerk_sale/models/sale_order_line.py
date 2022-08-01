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


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    description_html = fields.Html(
        string='HTML Description',
    )
    is_empty_description_html = fields.Boolean(
        compute='_compute_is_empty_description_html',
    )

    @api.depends('description_html')
    def _compute_is_empty_description_html(self):
        for record in self:
            record.is_empty_description_html = is_html_empty(
                record.description_html
            )
