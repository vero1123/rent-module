# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class product (models.Model):
    _inherit = 'product.template'

    daily_rent = fields.Float(string="Daily Rent")

class invoice(models.Model):
    _inherit = 'account.move.line'


    start_date = fields.Date(string="start date")
    end_date = fields.Date(string="end date")
    total_days = fields.Integer(string="total days")
    daily_rent = fields.Float(string="Daily Rent")
    total_cost = fields.Integer(string="total cost")


class rent(models.Model):
    _name = 'product.order'


    customer_id= fields.Many2one('res.partner',string="Customer Name")
    product_order_line_ids = fields.One2many('product.order.line','product_order_id',string='Product Lines')




    def create_invoice(self):

                res = self.env['account.move'].create({
                            'type': 'out_invoice',
                           'partner_id':self.customer_id.id,
                'invoice_line_ids': [(0, 0, {
                    'product_id': self.product_order_line_ids.product_id.id,
                    'start_date': self.product_order_line_ids.start_date,
                    'end_date': self.product_order_line_ids.end_date,
                    'total_cost': self.product_order_line_ids.total_cost,
                    'daily_rent': self.product_order_line_ids.daily_rent,
                    'total_days': self.product_order_line_ids.total_days,
                })],
            })


class productorderline(models.Model):

    _name ='product.order.line'

    product_order_id = fields.Many2one('product.order', string='Product Order')
    product_id = fields.Many2one('product.template',string='product')

    start_date = fields.Date(string="start date")
    end_date = fields.Date(string="end date")
    total_days = fields.Integer(string="total days",compute='_compute_days')
    daily_rent = fields.Float(related='product_id.daily_rent',string="Daily Rent")
    total_cost = fields.Integer(string="total cost",compute='_compute_cost')


    @api.depends('start_date','end_date')
    def _compute_days(self):
        for rec in self:
            if rec.start_date and rec.end_date:
               rec.total_days = (rec.end_date - rec.start_date).days
            else:
                rec.total_days=0




    @api.depends('total_days','daily_rent')
    def _compute_cost(self):
        for rec in self:
            rec.total_cost = rec.daily_rent*rec.total_days



