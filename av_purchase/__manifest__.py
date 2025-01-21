{
    "name": "Av Purchase",
    "author":"Serge",
    "version": "17.0.1.0",
    "category": "Av Puchase",
    "depends": ["base","mail","purchase"],
    'license': 'LGPL-3',
    "installable":True,
    "application": True,
    'summary': 'Manage purchases',
    "description": """
        A module for managing puchases.
    """,
    "data": [
        # SECURITY
        "security/res_groups.xml",
        "security/ir.model.access.csv",

        # VIEWS

        # REPORT
    ],
    "demo":[
    ],
}
