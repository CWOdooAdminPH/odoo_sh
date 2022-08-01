from odoo import _, api, fields, models, SUPERUSER_ID
from odoo.osv import expression


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    project_name = fields.Char(
        string='Project - Id',
    )

    def name_get(self):
        res = super().name_get()

        for i in range(len(res)):
            sale = self.browse(res[i][0])
            if not sale.project_name:
                continue

            res[i] = (res[i][0], '%s [%s]' % (res[i][1], sale.project_name))

        return res

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        if not (name or '').strip() and operator == 'ilike':
            return super()._name_search(
                name=name, args=args, operator=operator, limit=limit
            )

        domain = [
            '|',
            (self._rec_name, operator, name),
            ('project_name', operator, name)
        ]

        # 'sale' module
        if self._context.get('sale_show_partner_name'):
            if operator in ('ilike', 'like', '=', '=like', '=ilike'):
                domain = expression.OR([
                    domain, [
                        ('partner_id.name', operator, name)
                    ]
                ])

        # 'sale_expense' module
        if self._context.get('sale_expense_all_order'):
            name_get_uid = SUPERUSER_ID
            domain = expression.AND([
                domain, [
                    ('state', '=', 'sale'),
                    ('company_id', 'in', self.env.companies.ids)
                ]
            ])

        domain = expression.OR([args or [], domain])

        return self._search(
            domain,
            limit=limit,
            access_rights_uid=name_get_uid
        )

    def _prepare_analytic_account_data(self, prefix=None):
        vals = super()._prepare_analytic_account_data(prefix=prefix)

        if not self.project_name:
            return vals

        name = self.project_name
        if prefix:
            name = prefix + ": " + name

        vals.update({
            'name': name
        })

        return vals

    def _compute_l10n_de_document_title(self):
        project_set = self.filtered(lambda s: s.project_name)
        super(SaleOrder, self - project_set)._compute_l10n_de_document_title()

        for record in project_set:
            title = '%s - ' + record.project_name
            if record.state in ('draft', 'sent'):
                record.l10n_de_document_title = title % _('Quotation')
            else:
                record.l10n_de_document_title = title % _('Sales Order')

    def _compute_l10n_de_template_data(self):
        super()._compute_l10n_de_template_data()

        for record in self:
            data = record.l10n_de_template_data
            position = len(data) -1 if record.user_id else len(data)

            if record.user_id.phone:
                record.l10n_de_template_data.insert(
                    position, (_('Phone'), record.user_id.phone)
                )

            record.l10n_de_template_data.insert(
                position, (_('Order address'), 'orders@codewerk.de')
            )
