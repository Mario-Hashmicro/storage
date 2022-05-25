# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class AccountingCancelWizard(models.TransientModel):

    _name = "accounting.cancel.wizard"
    _description = "Accounting Cancel Reason Wizard"

    reasons = fields.Char(string='Reason', required=True)

    def recurring_cancel_reason(self):
        self.ensure_one()
        recurring = self.env['invoice.recurring'].browse(self._context.get('active_ids', []))
        recurring.reasons = self.reasons
        recurring.cancel()

        # print('res=====================')
        # if self.invoice_recurring:
        #     print(self.invoice_recurring, 'res=====================')
        #     self.invoice_recurring.cancel()
        # return {'type': 'ir.actions.act_window_close'}
