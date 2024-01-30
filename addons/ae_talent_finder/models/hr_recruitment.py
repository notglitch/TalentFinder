# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, SUPERUSER_ID

class TalentFinder(models.Model):
    _name = "ae.talent.finder"
    _description = "Looking for Talents"

    name = fields.Char("Porpouse", help="Declare the Purpose of the search", required=True)
    skill_ids = fields.Many2many('hr.skill', store=True)
    employees_skill_ids = fields.Many2many('hr.employee.skill', store=True)

    def add_matches(self):
        if self.skill_ids:
            self.employees_skill_ids = self.employees_skill_idsemployees_skill_id










