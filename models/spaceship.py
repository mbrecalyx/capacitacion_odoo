from odoo import models, fields


class Spaceship(models.Model):
    _name = "capacitacion_odoo.spaceship"
    _description = "Spaceship Information"

    name = fields.Char(string="Name")
    active = fields.Boolean(string="Active", default=True)
    type = fields.Selection(
        [
            ("carga", "Carga"),
            ("transporte", "Transporte"),
            ("exploracion", "Exploracion"),
            ("batalla", "Batalla"),
        ],
        string="Type",
    )
    modelo = fields.Char(string="Model", required=True)
    build_date = fields.Date(string="Build Date")
    captain = fields.Char(string="Captain")
    required_crew = fields.Integer(string="Required Crew")
    length = fields.Float(string="Length")
    width = fields.Float(string="Width")
    engine_number = fields.Char(string="Engine Number")
    fuel_type = fields.Selection(
        [("solid_fuel", "Solid Fuel"), ("liquid_fuel", "Liquid Fuel")],
        string="Fuel Type",
    )
    # Add any other fields here
