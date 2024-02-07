# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, SUPERUSER_ID

class TalentFinder(models.Model):
    _name = "ae.talent.finder"
    _description = "Looking for Talents"

    name = fields.Char("Porpouse", help="Declare the Purpose of the search", required=True)
    skill_ids = fields.Many2many('hr.skill.level', store=True, string='Skills')
    employees_skill_ids = fields.Many2many('hr.employee.skill', string='Employees with Skills', compute='_compute_employees_with_skills', store=True)
    applicants_skill_ids = fields.Many2many('hr.applicant', string='Applicants with Skills', compute='_compute_applicants_with_skills', store=True)
    selection_output = fields.Selection([
        ('employee', 'Employees'),
        ('applicant', 'Applicants'),
    ], string='Do the search for', default='applicant')
    @api.depends('skill_ids')
    def _compute_employees_with_skills(self):
        for talent_finder in self:
            skill_ids = talent_finder.skill_ids.ids
            employees_with_skills = self.env['hr.employee.skill'].search([('skill_id', 'in', skill_ids)])
            talent_finder.employees_skill_ids = [(6, 0, employees_with_skills.ids)]

    @api.depends('skill_ids')
    def _compute_applicants_with_skills(self):
        for talent_finder in self:
            applicant_ids = []
            skill_ids = talent_finder.skill_ids.ids
            applicants_with_skills = self.env['hr.applicant.skill'].search([('skill_id', 'in', skill_ids)])
            applicant_ids.extend(applicants_with_skills.mapped('applicant_id').ids)
            talent_finder.applicants_skill_ids = [(6, 0, applicant_ids)]














