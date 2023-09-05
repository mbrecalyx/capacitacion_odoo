from odoo import models, fields


class Task(models.Model):
    _name = "your_module_name.task"
    _description = "Task Information"

    name = fields.Char(string="Name")
    start_time = fields.Datetime(string="Start Time")
    stop_time = fields.Datetime(string="Stop Time")
    occurrences = fields.Integer(string="Occurrences")
    description = fields.Text(string="Description")
    task_type = fields.Selection(
        [
            # Add task types here
        ],
        string="Task Type",
    )
    # Add any other fields here
