{
    "name": "Av Project",
    "author":"Serge",
    "version": "17.0.1.0",
    "category": "Av Project",
    "depends": ["base","mail","project"],
    'license': 'LGPL-3',
    "installable":True,
    "application": False,
    'summary': 'Manage project',
    "description": """
        A module for managing project.
    """,
    "data": [
        # SECURITY
        "security/res_groups.xml",
        "security/ir.model.access.csv",

        # VIEWS
        "views/project_project_views.xml",

        # REPORT
    ],
    "demo":[
    ],
}
