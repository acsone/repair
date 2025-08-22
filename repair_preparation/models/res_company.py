# Copyright 2025 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResCompany(models.Model):

    _inherit = "res.company"

    repair_preparation_enabled = fields.Boolean(
        string="Enable Repair Preparation",
        help="If disabled, no preparation procurements/pickings will be created and "
        "repairs can be finished without preparation checks.",
    )

    repair_preparation_picking_type_id = fields.Many2one(
        "stock.picking.type",
        string="Default Preparation Operation Type",
        help="Default operation type used to bring spare parts to the Preparation area "
        "before the repair starts.",
        domain="[('code', '=', 'internal'), ('warehouse_id.company_id', '=', id)]",
    )
