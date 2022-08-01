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
{
	'name': 'Codewerk Sale Extensions',
	'version': '15.0.1.0.0',
	'summary': '',
	'category': 'Sales/Sales',
	'author': 'Openfellas',
	'company': 'Openfellas GmbH',
	'website': 'https://openfellas.com',
	'depends': [
		'sale_management',
	],
	'data': [
		'security/ir.model.access.csv',
        'wizards/custom_description_html_view.xml',
        'views/sale_order_views.xml',
		'views/sale_order_template_views.xml',
		'reports/sale_portal_templates.xml',
        'reports/sale_report_templates.xml',
	],
	'assets': {
		'web.report_assets_common': [
			'codewerk_sale/static/src/scss/sale_report.scss'
		],
		'web.assets_frontend': [
			'codewerk_sale/static/src/scss/sale_portal.scss',
		],
		'web.assets_backend': [
			'codewerk_sale/static/src/js/backend/**/*',
		],
	},
	'license': 'AGPL-3',
}
