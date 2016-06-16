# -*- coding: utf-8 -*-
# © <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import _, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    is_additional = fields.Boolean(
        string=_(u'Is additional'),
        select=False,
        help=_(u'It indicates whether this invoice was automatically \
               generated by being additional')
    )
    integration_id = fields.Many2one(
        'integration.cost.gebesa',
        string=_(u'integration',),
        help=_(u'Integration which is linked to a purchase'),
    )