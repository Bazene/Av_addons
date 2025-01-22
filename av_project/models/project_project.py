from odoo import models, fields, api


class Project(models.Model):
    # Meta data
    _inherit = "project.project"


    # Usual Fields
    project_budget = fields.Monetary(string="Budget", store=True)
    currency_id = fields.Many2one("res.currency", string="Currency",default=lambda self: self.env.company.currency_id)
    user_id = fields.Many2one("hr.employee", string="HOD", readonly=True, compute="_compute_hod", store=True)

    # Related fields
    department_id = fields.Many2one("hr.department", string="Department", domain="[('manager_id', '!=', False)]", help="Department where a HOD exists")


    # Functions
    @api.depends("department_id")
    def _compute_hod(self):
        for record in self:
            if record.department_id:
                record.user_id = record.department_id.manager_id
            else:
                record.user_id = False
