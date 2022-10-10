# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Some estate information"

    title = fields.Char('Plan Name', required=True, translate=True)
    property_type = fields.Char('Property Type', required=True, translate=True)
