# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from collections import Counter


class Lead(models.Model):
    _inherit = 'crm.lead'

    lead_skill_ids = fields.One2many('crm.lead.skills', 'lead_id', string="Skills")
    skill_ids = fields.Many2many('hr.skill', compute='_compute_skill_ids', store=True)
    employee_skill_ids = fields.Many2many('hr.employee.skill', string="Employee Skills")
    matching_rating = fields.One2many('lead.matching.rating', 'lead_id', string="Matching Rating")

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

    def compute_matching_rating(self):
        self.ensure_one()
        matching_rating_values = {}
        matching_employees_set = set()
        for employee_skill in self.employee_skill_ids:
            combination = (
            employee_skill.skill_id.id, employee_skill.skill_type_id.id, employee_skill.skill_level_id.id,
            employee_skill.employee_id.id)
            if combination not in matching_employees_set:
                matching_employees = self.env['hr.employee.skill'].search_count([
                    ('skill_id', '=', employee_skill.skill_id.id),
                    ('skill_type_id', '=', employee_skill.skill_type_id.id),
                    ('skill_level_id', '=', employee_skill.skill_level_id.id),
                    ('employee_id', '=', employee_skill.employee_id.id),
                ])
                matching_employees_set.add(combination)
                matching_rating_values[employee_skill.employee_id.id] = matching_rating_values.get(
                    employee_skill.employee_id.id, 0) + matching_employees
        for employee_id, rating in matching_rating_values.items():
            lead_matching_rating = self.matching_rating.filtered(lambda r: r.employee_id.id == employee_id)
            if lead_matching_rating:
                lead_matching_rating.write({'matching_rating': rating})
            else:
                self.matching_rating.create({
                    'lead_id': self.id,
                    'employee_id': employee_id,
                    'matching_rating': rating,
                })
        self.matching_rating = self.matching_rating.sorted(key=lambda r: r.matching_rating, reverse=True)

    def button_matches_rating(self):
        self.compute_matching_rating()


class LeadMatchingRating(models.Model):
    _name = 'lead.matching.rating'
    _description = "Matching Rating"
    _order = 'matching_rating desc'

    lead_id = fields.Many2one('crm.lead', string="Lead")
    employee_id = fields.Many2one('hr.employee', string="Employee")
    job_id = fields.Many2one('hr.job', related="employee_id.job_id")
    department_id = fields.Many2one('hr.department', related="employee_id.department_id")
    matching_rating = fields.Integer(string="Matching Rating")
    employee_skill_ids = fields.Many2many('hr.employee.skill', string="Employee Skills")

    def show_employee_skills(self):
        view_id = self.env.ref('hr_skills.employee_skill_view_form').id
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hr.employee.skill',
            'view_id': view_id,
            'res_id': self.employee_id.id,
            'target': 'current',
        }


class HRSkill(models.Model):
    _inherit = 'hr.employee.skill'

    job_id = fields.Many2one('hr.job', related="employee_id.job_id")
    department_id = fields.Many2one('hr.department', related="employee_id.department_id")
