# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Talent Finder CRM',
    'version': '16.0.1',
    'category': 'CRM',
    'author': "Aleph Engineering",
    'website': "https://aleph.engineering",
    'summary': 'Pick up each lead  that require very specific skills from your employees',
    'depends': [
        'hr',
        'hr_skills',
        'crm',
    ],
    'data': [
        "security/ir.model.access.csv",
        "views/crm_lead_skills_views.xml",

    ],
    'installable': True,
    'application': True,
}
