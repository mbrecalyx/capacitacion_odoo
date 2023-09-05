from odoo import models, fields


class Book(models.Model):
    _name = "your_module_name.book"
    _description = "Book Information"

    name = fields.Char(string="Name")
    active = fields.Boolean(string="Active", default=True)
    isbn = fields.Char(string="ISBN")
    genre = fields.Char(string="Genre")
    summary = fields.Text(string="Summary")
    author = fields.Char(string="Author")
    book_format = fields.Selection(
        [
            ("Paperback", "Paperback"),
            ("Hardcover", "Hardcover"),
            ("Audiobook", "Audiobook"),
            ("E-Book", "E-Book"),
        ],
        string="Book Format",
    )
    language = fields.Selection(
        [("en", "English"), ("es", "Spanish"), ("fr", "French"), ("de", "German")],
        string="Language",
    )
    edition = fields.Integer(string="Edition")
    publisher = fields.Char(string="Publisher")
    publish_date = fields.Date(string="Publish Date")
    price = fields.Monetary(string="Price")
    # Add any other fields here
