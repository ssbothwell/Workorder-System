"""
Validation Helpers
"""
from schema import Schema, And

# JSON Request schemas
client_schema = Schema(And({'first_name': str,
                            'last_name': str,
                            'email': str,
                            'phone': str}))


strainer_schema = Schema(And({'project_id': int,
                              'width': int,
                              'height': int,
                              'thickness': int,
                              'price': int,
                              'quantity': int,
                              'total': int,
                              'notes': str
                             }))


panel_schema = Schema(And({'project_id': int,
                           'width': int,
                           'height': int,
                           'thickness': int,
                           'price': int,
                           'quantity': int,
                           'total': int,
                           'notes': str
                          }))


pedestal_schema = Schema(And({'project_id': int,
                              'width': int,
                              'height': int,
                              'depth': int,
                              'price': int,
                              'quantity': int,
                              'total': int,
                              'notes': str
                             }))


custom_project_schema = Schema(And({'project_id': int,
                                    'price': int,
                                    'quantity': int,
                                    'total': int,
                                    'notes': str
                                   }))


project_schema = Schema(And({'client_id': int,
                             'due_date': str,
                             'completion_date': str,
                             'project_title': str,
                             'status': int,
                             'deposit': int,
                             'discount': int,
                             'strainer_bars': [strainer_schema],
                             'panels': [panel_schema],
                             'pedestals': [pedestal_schema],
                             'custom_projects': [custom_project_schema]
                            }))
