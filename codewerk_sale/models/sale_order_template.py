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

from odoo import fields, models


class SaleOrderTemplate(models.Model):
    _inherit = 'sale.order.template'

    header_html = fields.Html(
        string='HTML Header',
    )
