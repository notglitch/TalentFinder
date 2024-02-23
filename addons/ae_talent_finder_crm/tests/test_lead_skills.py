from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError

class TestMatchingEmployees(TransactionCase):

    def setUp(self):
        super(TestMatchingEmployees, self).setUp()
        self.lead_model = self.env['crm.lead']
        self.employee_skill_model = self.env['hr.employee.skill']

    def test_find_matching_employees(self):
        # Create a lead record with specific skills
        lead = self.lead_model.create({
            'name': 'Test Lead',
        })
        lead_skill_data = {
            'lead_id': lead.id,
            'skill_id': self.env.ref('module.skill_1').id,
            'skill_type_id': self.env.ref('module.skill_type_1').id,
            'skill_level_id': self.env.ref('module.skill_level_1').id,
        }
        self.env['crm.lead.skills'].create(lead_skill_data)

        # Create some employee skill records
        employee_skills_data = [
            {
                'employee_id': self.env.ref('module.employee_1').id,
                'skill_id': self.env.ref('module.skill_1').id,
                'skill_type_id': self.env.ref('module.skill_type_1').id,
                'skill_level_id': self.env.ref('module.skill_level_1').id,
            },
            {
                'employee_id': self.env.ref('module.employee_2').id,
                'skill_id': self.env.ref('module.skill_2').id,
                'skill_type_id': self.env.ref('module.skill_type_2').id,
                'skill_level_id': self.env.ref('module.skill_level_2').id,
            },
        ]
        self.employee_skill_model.create(employee_skills_data)

        # Call the method to find matching employees
        lead.find_matching_employees()

        # Check if matching employees have been assigned correctly
        self.assertTrue(lead.employee_skill_ids, "No matching employees found")
        self.assertEqual(len(lead.employee_skill_ids), 1, "The number of matching employees is incorrect")
