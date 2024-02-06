
from odoo import models, fields, api


class pedido(models.Model):
    _name = 'odoo_basico.pedido'
    _description = 'exemplo de pedido:'
    _sql_constraints = [("nomeUnico", "unique(name)", "O Identificador de pedido debe ser único")]

    name = fields.Char(required=True, size=20, string="Identificador de Pedido:")
    lineapedido_ids = fields.One2many("odoo_basico.lineapedido", 'pedido_id')
