# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductDiscount(models.Model):
    _inherit = ['res.config.settings']

    prod_discount = fields.Float(string='Product Discount')
