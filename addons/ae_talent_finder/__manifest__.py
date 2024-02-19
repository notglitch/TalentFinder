# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Talent Finder',
    'version': '16.0.1',
    'category': 'Human Resources/Recruitment',
    'author': "Aleph Engineering",
    'website': "https://aleph.engineering",
    'summary': 'Find the best talents to join your work team',
    'depends': [
        'hr',
        'hr_recruitment_skills',
        'hr_recruitment',
        'crm',
        'project',
    ],
    'data': [
	"views/hr_recruitment_views.xml",
    "security/ir.model.access.csv",

    ],
    'installable': True,
    'application': True,
}
