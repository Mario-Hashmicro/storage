from odoo import api, fields, models

class AccountingRecurring(models.Model):
    _inherit = "invoice.recurring"

    reasons = fields.Char(string='Reason')

    def cancel_override(self):
        self.write({'state': 'cancel'})
        view_id = self.env.ref('cipi_accounting_recurring_invoices.cancel_form_view').id
        return {
            #'name': self.order_id,
            'view_type':'form',
            'view_mode':'form',
            'views' : [(view_id,'form')],
            'res_model':'invoice.recurring',
            'view_id':view_id,
            'type':'ir.actions.act_window',
            'res_id':self.id,
            'target':'new',
            'context':{},
        }

   