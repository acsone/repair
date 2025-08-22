# Copyright 2025 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    repair_preparation_enabled = fields.Boolean(
        related="company_id.repair_preparation_enabled", readonly=False
    )

    repair_preparation_picking_type_id = fields.Many2one(
        "stock.picking.type",
        related="company_id.repair_preparation_picking_type_id",
        readonly=False,
        domain="[('code', '=', 'internal'), ('warehouse_id.company_id', '=', company_id)]",
    )
