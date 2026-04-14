# Copyright 2026 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class RepairOrder(models.Model):
    _inherit = "repair.order"
    state = fields.Selection(
        selection_add=[("confirmed",), ("sent", "Quotation Sent"), ("done",)],
        ondelete={"sent": "set confirmed"},
    )
    quotation_sent = fields.Boolean(readonly=True)

    def write(self, vals):
        res = super().write(vals)
        if vals.get("quotation_sent") and (
            to_update_records := self.filtered(
                lambda ro: ro.state in ("draft", "confirmed")
            )
        ):
            to_update_records.state = "sent"
        return res

    def action_repair_start(self):
        """Allow starting repairs from 'sent' by temporarily shifting state."""
        sent_repairs = self.filtered(lambda r: r.state == "sent")

        if sent_repairs:
            sent_repairs.update({"state": "confirmed"})

        try:
            return super().action_repair_start()
        except Exception:
            if sent_repairs:
                sent_repairs.update({"state": "sent"})
            raise
