from odoo import models, fields


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate property offers"
    _order = "id desc"

    price = fields.Integer()
    status = fields.Selection(string='Status', copy=False,
                              selection=[('accepted', 'Accepted'),
                                         ('refused', 'Refused')])

    # relations
    partner_id = fields.Many2one('res.partner', string='Partner')
    property_id = fields.Many2one('estate.property', string='Property')
