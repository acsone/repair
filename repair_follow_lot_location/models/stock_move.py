# Copyright 2025 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class StockMove(models.Model):

    _inherit = "stock.move"

    def _action_done(self, cancel_backorder=False):
        res = super()._action_done(cancel_backorder=cancel_backorder)
        done_moves = self.filtered(lambda m: m.state == "done")
        if not done_moves:
            return res
        lots = done_moves.move_line_ids.lot_id
        if not lots:
            return res
        repair_orders = self.env["repair.order"].search(
            [
                ("follow_lot_location", "=", True),
                ("lot_id", "in", lots.ids),
                ("state", "not in", ["done", "cancel"]),
            ]
        )
        for repair_order in repair_orders:
            move = done_moves.filtered(
                lambda m, lot=repair_order.lot_id: lot in m.move_line_ids.lot_id
            )
            repair_order.location_id = move.location_dest_id[:1]
        return res
