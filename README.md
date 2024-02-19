<h3>About Talent Finder</h3>
***
Odoo manages talents from the application of human resources, considering employees and applicants as
well as the skills and competencies required to fill jobs.
However, the search for talent to form work teams may be necessary from other flows, even from the beginning of commercial processes. Talent Finder has been designed based on the need that may exist, to know in advance if the company has sufficiently 
competitive personnel to take on new projects as soon as a business opportunity appears with specific requirements.
The functionalities of this module must radiate throughout the processes where it can be applied: CRM, Project, Recruitment.

<h3>Main Idea</h3>
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
* [Technical Features](#technical-features)
* [Functional Features](#functional-features)
* [Functional and technical requirements that must be improved in future releases](#functional-and-technical-requirements-that-must-be-improved-in-future-releases)
  * [CRM Talent Finder](#crm-talent-finder)
  * [Project Talent Finder](#project-talent-finder)
  * [Recruitment Talent Finder](#recruitment-talent-finder)
* [Desired Collaboration](#desired-collaboration)
* [Write down your ideas and share them...](#write-down-your-ideas-and-share-them)

### Technical Features
*** 
Technical Name: ae_talent_finder
    
    'name': 'Talent Finder',
    'version': '16.0.1',
    'category': 'Human Resources/Recruitment',
    'author': "Aleph Engineering",
    'website': "https://aleph.engineering",
    'summary': 'Find the best talents to join your work team',
    'depends': [
        'hr_recruitment_skills',
        'hr_skills',
        'crm',
        'project',
    ],
  
### Functional Features
*** 
    * The user will be able to define the purpose of the search: defining a name and indicating the origin
        * If the origin is CRM, you can choose the lead to which it relates 
        * If the origin is Project, you can choose the project to which it is related 
        * By default the origin recruitment is selected already 
    * For all cases, the user will be able to define the skills they need;
        * and when choosing whether the system should show employees or applicants, 
        * those who have the defined skills will be shown without distinction.


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

   
##### Project Talent Finder
***
   * #### Technical Features
     Technical Name: ae_talent_finder_project

            'name': 'Project Talent Finder',
            'version': '14.1',
            'category': 'Project',
            'author': "Aleph Engineering",
            'website': "https://aleph.engineering",
            'summary': 'Find applicants whose levels of skills correspond to the specifications and peculiar needs of a project',
            'depends': [
                'hr_recruitment_skills',
                'project',
            ],
   * #### Functional Features 
       ***
         * Pick up projects with development requirements that require very specific skills with an specific levels 
         * Find all those applicants who have the required skill levels 
         * Show the best matches based on a limit of people.

##### Recruitment Talent Finder
***
   * #### Technical Features
     Technical Name: ae_talent_finder_recruitment
      
            'name': 'Recruitmente Talent Finder',
            'version': '16.0.1',
            'category': 'Human Resources/Recruitment',
            'author': "Aleph Engineering",
            'website': "https://aleph.engineering",
            'summary': 'Find applicants or employees whose skills levesl match with needs requested by the other areas of the company',
            'depends': [
                'hr_recruitment_skills',
                'hr_skills',
            ],
     #### Functional Features
        
            * Respond as service to other areas of the company that demand people with very specific skills with an specific levels 
            * Find all those employees and applicants who have the required skill levels.
            * Show the best matches based on a limit of people.

### Desired Collaboration
***
Please feel free to contribute to the functional and technical improvement of our module.
1. [ ] Should a functionality be inserted to notify employees or applicants of the availability to participate in integrating the new crew? 
2. [ ] Should a report be generated with those selected?
3. [ ] Should a round system be established based on: Best Matches, Second Choices and Approximate Matches?

###### Write down your ideas and share them in the space: [Welcome suggestions and questions](/opt/odoo/odoo16/addons/ae_talent_finder/Welcome suggestions and questions.md)

### Fast guide on how to leave your comments and suggestions
1. Put this file in editable mode
2. Copy the following structure that appears between lines, including the lines 
   3. and paste it at the end of the last comment. 
   3. Complete the information requested in each section of the copied and stuck structure

_Thanks for sharing..._ 

---------------------------------
#### Title: <Write here a summary title of your comment.Delete the symbols of greater than and less than at the beginning and the end of the sentence>
#### User: <Write your user name and Company.Delete the symbols of greater than and less than at the beginning and the end of the sentence>
#### Questions: 
    1. Write a Questions
    2. Write a Questions
    3. Write a Questions
#### Suggestions: 
    1. Write a Suggestions
    2. Write a Suggestions
    3. Write a Suggestions
#### Do yoy like this solution?
<Mark an X in the box that corresponds to your answer without spaces>

1. [ ]  Yes 
2. [ ]  No
3. [ ]  It needs a lot of Improvements
---------------------------------



