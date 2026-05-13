# Copyright 2025 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class StockMove(models.Model):
    _inherit = "stock.move"

    def init(self):
        """
        Add a partial index on repair_id to optimize filtering.
        Standard Odoo does not index this field in stock.move.
        """
        res = super().init()
        index_name = "stock_move_repair_id_partial_index"
        query = f"""
            CREATE INDEX IF NOT EXISTS {index_name}
            ON stock_move (repair_id)
            WHERE repair_id IS NOT NULL
            """
        # pylint: disable=sql-injection
        self.env.cr.execute(query)
        return res

    def _action_done(self, cancel_backorder=False):
        repair_moves = self.browse()
        if self.env.context.get("dont_validate_repair_move"):
            repair_moves = self.filtered("repair_id")

        return super(StockMove, self - repair_moves)._action_done(
            cancel_backorder=cancel_backorder
        )
