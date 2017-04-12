# -*- coding: utf-8 -*-
# © <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    move_name = fields.Char(
        string='Journal Entry',
        readonly=False,
        default=False,
        copy=False,
        help="Technical field holding the number given to the invoice, \
        automatically set when the invoice is validated then stored \
        to set the same number again if the invoice is cancelled, \
        set to draft and re-validated.")

    @api.multi
    def do_cfdi_workflow(self):
        for line in self.invoice_line_ids:
            if line.product_id.id in (975887, 975888, 507890):
                return []
        return super(AccountInvoice, self).do_cfdi_workflow()


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    @api.model
    def create(self, vals):
        line = super(AccountInvoiceLine, self).create(vals)
        line.invoice_id.compute_taxes()
        return line
