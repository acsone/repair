# Copyright 2026 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class MailComposeMessage(models.TransientModel):

    _inherit = "mail.compose.message"

    def _action_send_mail(self, auto_commit=False):

        use_custom_email_from = self.env.company.use_custom_repair_sender
        custom_email_from = self.env.company.repair_custom_email_from

        if self.model == "repair.order" and use_custom_email_from and custom_email_from:
            for rec in self:
                rec.email_from = custom_email_from

        return super()._action_send_mail(auto_commit=auto_commit)
