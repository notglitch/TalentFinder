# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from collections import Counter


class EmployeeSkill(models.Model):
    _inherit = 'hr.employee.skill'

    weight = fields.Float("Weight")
    is_repeated = fields.Boolean('Repeated', compute='_compute_is_repeated')

    @api.depends('employee_id', 'skill_id')
    def _compute_is_repeated(self):
        for record in self:
            count = self.search_count([
                ('id', '!=', record.id),  # Excluir el propio registro
                ('employee_id', '=', record.employee_id.id),
                ('skill_id', '=', record.skill_id.id)
            ])
            record.is_repeated = count > 0


class Lead(models.Model):
    _inherit = 'crm.lead'

    lead_skill_ids = fields.One2many('crm.lead.skills', 'lead_id', string="Skills")
    skill_ids = fields.Many2many('hr.skill', compute='_compute_skill_ids', store=True)
    employee_skill_ids = fields.Many2many('hr.employee.skill', string="Employee Skills")

    @api.depends('lead_skill_ids.skill_id')
    def _compute_skill_ids(self):
        for lead in self:
            lead.skill_ids = lead.lead_skill_ids.skill_id

    def find_matching_employees(self):
        matching_employees = self.env['hr.employee.skill']

        for lead_skill in self.lead_skill_ids:
            employees_with_matching_skills = self.env['hr.employee.skill'].search([
                ('skill_id', '=', lead_skill.skill_id.id),
                ('skill_type_id', '=', lead_skill.skill_type_id.id),
                ('skill_level_id', '=', lead_skill.skill_level_id.id),
            ])
            matching_employees |= employees_with_matching_skills

        self.employee_skill_ids = [(6, 0, matching_employees.ids)]

    def button_best_matches(self):
        self.find_matching_employees()

    def assign_weights_to_employees(self):
        employee_counter = Counter(self.employee_skill_ids.mapped('employee_id'))
        for employee_skill in self.employee_skill_ids:
            employee_id = employee_skill.employee_id
            repetitions = employee_counter.get(employee_id, 0)
            weight = repetitions
            employee_skill.write({'weight': weight})

