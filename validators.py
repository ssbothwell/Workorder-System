"""
Validation Helpers
"""
from schema import Schema, And, Use, Optional
import json

# JSON Request schemas
client_schema = Schema(And({'first_name': str,
                            'last_name': str,
                            'email': str,
                            'phone': str}))


strainer_schema = Schema(And({'project_id': int,
                              'width': float,
                              'height': float,
                              'thickness': float,
                              'price': int,
                              'notes': str
                             }))


panel_schema = Schema(And({'project_id': int,
                           'width': float,
                           'height': float,
                           'thickness': float,
                           'price': int,
                           'notes': str
                          }))


pedestal_schema = Schema(And({'project_id': int,
                             'width': float,
                             'height': float,
                             'depth': float,
                             'price': int,
                             'notes': str
                             }))


custom_project_schema = Schema(And({'project_id': int,
                                    'price': int,
                                    'notes': str
                                   }))


project_schema = Schema(And({'client_id': int,
                             'creat_date': str,
                             'due_date': str,
                             'completion_date': str,
                             'project_title': str,
                             'status': int,
                             'deposit': int,
                             'disount': int,
                             'strainer_bars': [strainer_schema],
                             'panels': [panel_schema],
                             'pedestals': [pedestal_schema],
                             'custom_projects': [custom_project_schema]
                            }))
