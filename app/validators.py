"""
Validation Helpers
"""
from schema import Schema, And, Or, Optional

# JSON Request schemas
client_schema = Schema(And({'first_name': str,
                            'last_name': str,
                            'email': str,
                            'phone': str,
                           }))


strainer_schema = Schema(And({Optional('project_id'): int,
                              'width': int,
                              'height': int,
                              'thickness': float,
                              'price': int,
                              'quantity': int,
                              'total': int,
                              'notes': str,
                              'p_type': str
                             }))


panel_schema = Schema(And({Optional('project_id'): int,
                           'width': int,
                           'height': int,
                           'thickness': int,
                           'price': int,
                           'quantity': int,
                           'total': int,
                           'notes': str,
                           'p_type': str
                          }))


pedestal_schema = Schema(And({Optional('project_id'): int,
                              'width': int,
                              'height': int,
                              'depth': int,
                              'price': int,
                              'quantity': int,
                              'total': int,
                              'notes': str,
                              'p_type': str
                             }))


custom_project_schema = Schema(And({Optional('project_id'): int,
                                    'price': int,
                                    'quantity': int,
                                    'total': int,
                                    'notes': str,
                                    'p_type': str
                                   }))

line_item_schema = Schema(Or(strainer_schema,
                      panel_schema,
                      pedestal_schema,
                      custom_project_schema))

project_schema = Schema(And({'client_id': int,
                             'due_date': str,
                             'completion_date': str,
                             'project_title': str,
                             'status': int,
                             'deposit': int,
                             'discount': int,
                             'line_items': [line_item_schema]
                            }))
