from odoo import models, fields, api


class lineapedido(models.Model):
    _name = 'odoo_basico.lineapedido'
    _description = 'exemplo de lineapedido:'
    _order = "name asc"

    name = fields.Char(required=True, size=20, string="Identificador da línea de pedido")
    descripcion = fields.Text(string="Comentario da línea de pedido")
    pedido_id = fields.Many2one('odoo_basico.pedido',
                                ondelete="cascade", required=True)
