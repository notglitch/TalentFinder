
### About Talent Finder CRM
It corresponds to the need to modularize the Talent Finder solution. It is designed to help commercial specialists identify work teams or people that respond to the specific needs or requirements of certain clients of a lead. 
The search for suitable employees is carried out by matching the skills of the employees with the skills demanded by the new lead. The importance of this module is that from the early lead, you will be able to know if you have 
the necessary competent personnel to face a new business opportunity.

### About Talent Finder
***
Odoo manages talents from the application of human resources, considering employees and applicants as
well as the skills and competencies required to fill jobs.
However, the search for talent to form work teams may be necessary from other flows, even from the beginning of commercial processes. Talent Finder has been designed based on the need that may exist, to know in advance if the company has sufficiently 
competitive personnel to take on new projects as soon as a business opportunity appears with specific requirements.
The functionalities of this module must radiate throughout the processes where it can be applied: CRM, Project, Recruitment.


_This solution, and the solutions derived from Talent Finder, is being developed by **Aleph Engineer Company**_
*** 

### Main Idea
***
Find the talents whose skills are required with specific levels:
  1. For a potential client, valued as a lead for the company. In this case: Company Employees should be considered Talents.
  2. For a project that registers very specific requirements for its development, and requires Talents that satisfy these requirements. In this case: Company Employees and Applicants must be considered Talents.
  3. For a Recruitment process that has a pool of talents and that needs to find people whose skills match the levels requested by the other areas of the company. In this case: Applicants should be considered Talents.

### Project status

| Status Items                    | Stages/Description                                                                                 |
|---------------------------------|----------------------------------------------------------------------------------------------------|
| Phase                           | Development                                                                                        |
| Odoo Current Version            | 16.0                                                                                               |
| Odoo version pending to migrate | 14.0                                                                                               |
| Current Solution Version        | Talent Finder 16.0.1                                                                               |
|                                 | Talent Finder 16.1                                                                                 |
| Planned Releases                | Talent Finder 14.1                                                                                 |
| Derived Solutions               | * CRM Talent Finder 14.1                                                                           |
|                                 | * Project Talent Finder 14.1                                                                       |
|                                 | * Recruitment Talent Finder 14.1                                                                   |
| Planned Actions                 | 1. Fix Noted Improvements                                                                          |
|                                 | 2. Migrate the Solution to Odoo 14.0                                                               |
|                                 | 3. Modularize the Solution in Odoo 14.0                                                            |
|                                 | 4. Integrate the modules to the Odoo flows of the Aleph Engineer Company                           |
|                                 | 5. Migrate modularization to Odoo 16.0 for the generic version and for Odoo Aleph Engineer Company |
###### Maybe you want to know about: the numbering of versions [https://ed.team/blog/como-se-deciden-las-versiones-del-software](https://ed.team/blog/como-se-deciden-las-versiones-del-software)

### Table of Content

* [Functional and technical requirements that must be improved in future releases](#functional-and-technical-requirements-that-must-be-improved-in-future-releases)
  * [CRM Talent Finder](#crm-talent-finder)
* [Desired Collaboration](#desired-collaboration)
* [Write down your ideas and share them...](#write-down-your-ideas-and-share-them)

### Functional and technical requirements that must be improved in future releases 
***
**_Structure this solution as modular_** is the main requirement and improvement noted.

Generates big technical and functional changes.

Which means that instead of having a single Talent Finder module that manages from a single place all the searches 
integrated with CRM, Project and Recruitment, there will be 3 modules, each one will do a talent search in its own flow. 
That means Talent Finder will be split in the modules:

 * CRM Talent Finder 
 * Project Talent Finder 
 * Recruitment Talent Finder

This requirement correspond to the Planned Actions: **_Modularize the Solution in Odoo 14.0_**, but also implies the actions:
1. Fix Noted Improvements               
2. Migrate the Solution to Odoo 14.0  

And when this actions be al ready done, the following steps will be:
4. Integrate the modules to the Odoo flows of the Aleph Engineer Company
5. Migrate modularization to Odoo 16.0 for the generic version and for Odoo Aleph Engineer Company


##### CRM Talent Finder
***
  * 
      #### Technical Features
     Technical Name: ae_talent_finder_crm
   
            'name': 'CRM Talent Finder',
            'version': '14.1',
            'category': 'Sales/CRM',
            'author': "Aleph Engineering",
            'website': "https://aleph.engineering",
            'summary': 'Find employees whose skills levels correspond to the peculiar specifications of your customers.',
            'depends': [
                'hr_skills',
                'crm',
            ],
     #### Functional Features 
     ***
        * Pick up each business opportunity (lead) with development requirements that require very specific skills with an specific levels 
        * Find all those employees who have the required skill levels 
        * Show the best matches based on a limit of people.

   

### Desired Collaboration
***
Please feel free to contribute to the functional and technical improvement of our module.
1. [ ] Should a functionality be inserted to notify employees or applicants of the availability to participate in integrating the new crew? 
2. [ ] Should a report be generated with those selected?
3. [ ] Should a round system be established based on: Best Matches, Second Choices and Approximate Matches?

###### Write down your ideas and share them in the space Welcome Suggestions and Questions:
###### addons/ae_talent_finder/Welcome suggestions and questions.md
https://github.com/notglitch/TalentFinder/blob/main/addons/ae_talent_finder/Welcome%20suggestions%20and%20questions.md


