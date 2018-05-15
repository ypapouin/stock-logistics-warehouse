# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    orderpoint_ids = fields.Many2many(
        comodel_name='stock.warehouse.orderpoint',
        string='Linked Reordering Rules',
    )

    def _prepare_procurement_values(self):
        res = super(StockMove, self)._prepare_procurement_values()
        if self.orderpoint_ids:
            res['orderpoint_ids'] = self.orderpoint_ids
        return res
