"""
Fabco Workorder System Unit Tests
Solomon Bothwell
"""
import unittest
import json
import config
from flask.wrappers import Response
from app import create_app, db
from app.models import Custom_Project, Project, Client


class TestProjectControllers(unittest.TestCase):
    """ Project controllers test cases """

    def setUp(self):
        self._app = create_app(config.TestingConfig)
        self._app.app_context().push()
        self.app = self._app.test_client()
        db.create_all()

        mock_json = {'first_name': 'first',
                     'last_name': 'user',
                     'email': 'first@user',
                     'phone': '1234567890',
                    }
        self.post_client(mock_json)

        mock_json = {"client_id": 1,
                     "due_date": "2018-01-01",
                     "completion_date": "2018-02-01",
                     "project_title": "a test project",
                     "status": 0,
                     "deposit": 5000,
                     "discount": 0,
                     "line_items": [{"price": 100,
                                     "quantity":2,
                                     "total": 200,
                                     "p_type": "custom_project",
                                     "notes": ""
                                    }]
                    }

        response = self.post_project(mock_json)


    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def post_client(self, mock_json: dict) -> Response:
        """
        Helper Function for adding Clients to database
        """
        headers = {'content-type': 'application/json'}
        response = self.app.post('/clients/new',
                                 data=json.dumps(mock_json),
                                 headers=headers)
        return response


    def post_project(self, mock_json: dict) -> Response:
        """
        Helper Function for adding Projects to database
        """
        headers = {'content-type': 'application/json'}
        response = self.app.post('/projects/new',
                                 data=json.dumps(mock_json),
                                 headers=headers)
        return response


    def get_project(self, ident: int) -> Response:
        """
        Helper Function for getting a project from database
        """
        headers = {'content-type': 'application/json'}
        response = self.app.get('/projects/{0}'.format(ident),
                                headers=headers)
        return response


    def delete_project(self, ident: int) -> Response:
        """
        Helper Function for deleting projects from database
        """
        headers = {'content-type': 'application/json'}
        response = self.app.delete('/projects/{0}/delete'.format(ident),
                                   headers=headers)
        return response


    def update_project(self, ident: int, mock_json: dict) -> Response:
        """
        Helper Function for updating projects in database
        """
        headers = {'content-type': 'application/json'}
        response = self.app.post('/projects/{0}/update'.format(ident),
                                 data=json.dumps(mock_json),
                                 headers=headers)
        return response


    def testCreateProject(self) -> None:
        """
        Create a new project
        """
        mock_json = {'client_id': 1,
                     'due_date': '2018-03-12',
                     'completion_date': '2018-03-15',
                     'project_title': 'another test project',
                     'status': 0,
                     'deposit': 500,
                     'discount': 0,
                     'line_items': [{'price': 100,
                                     'quantity':2,
                                     'total': 200,
                                     'width': 48,
                                     'height': 36,
                                     'thickness': 1,
                                     'p_type': 'strainer_bar',
                                     'notes': ''
                                    },
                                    {'price': 200,
                                     'quantity':3,
                                     'total': 600,
                                     'width': 72,
                                     'height': 60,
                                     'thickness': 1.25,
                                     'p_type': 'strainer_bar',
                                     'notes': ''
                                    }
                                    ]
                    }

        response = self.post_project(mock_json)
        self.assertEqual(response.status_code, 200)


    def testGetClient(self) -> None:
        """
        Get a client
        """
        response = self.get_project(1)
        self.assertEqual(response.status_code, 200)


    def testDeleteClient(self) -> None:
        """
        Delete a client
        """
        response = self.delete_project(1)
        self.assertEqual(response.status_code, 200)


    def testUpdateProject(self) -> None:
        """
        Update a project
        """
        mock_json = {"client_id": 1,
                     "due_date": "2018-01-01",
                     "completion_date": "2018-02-01",
                     "project_title": "a test project",
                     "status": 0,
                     "deposit": 5000,
                     "discount": 0,
                     "line_items": [{"price": 100,
                                     "quantity":2,
                                     "total": 200,
                                     "p_type": "custom_project",
                                     "notes": ""
                                    },
                                    {"price": 150,
                                     "quantity": 3,
                                     "total": 450,
                                     "width": 48,
                                     "height": 72,
                                     "thickness": 1,
                                     "p_type": "panel",
                                     "notes": ""
                                    }
                                    ]
                    }

        response = self.update_project(1, mock_json)
        self.assertEqual(response.status_code, 200)


class TestClientControllers(unittest.TestCase):
    """ Base test class """

    def setUp(self):
        self._app = create_app(config.TestingConfig)
        self._app.app_context().push()
        self.app = self._app.test_client()
        db.create_all()

        mock_json = {'first_name': 'first',
                     'last_name': 'user',
                     'email': 'first@user',
                     'phone': '1234567890',
                    }
        self.put_client(mock_json)
        mock_json = {'first_name': 'second',
                     'last_name': 'user',
                     'email': 'second@user',
                     'phone': '1234567890',
                    }
        self.put_client(mock_json)


    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def put_client(self, mock_json: dict) -> Response:
        """
        Helper Function for adding Clients to database
        """
        headers = {'content-type': 'application/json'}
        response = self.app.post('/clients/new',
                                 data=json.dumps(mock_json),
                                 headers=headers)
        return response


    def get_client(self, ident: int) -> Response:
        """
        Helper Function for getting a client from database
        """
        headers = {'content-type': 'application/json'}
        response = self.app.get('/clients/{0}'.format(ident),
                                headers=headers)
        return response


    def delete_client(self, ident: int) -> Response:
        """
        Helper Function for deleting Clients from database
        """
        headers = {'content-type': 'application/json'}
        response = self.app.delete('/clients/{0}/delete'.format(ident),
                                   headers=headers)
        return response


    def update_client(self, ident: int, mock_json: dict) -> Response:
        """
        Helper Function for updating Clients in database
        """
        headers = {'content-type': 'application/json'}
        response = self.app.post('/clients/{0}/update'.format(ident),
                                 data=json.dumps(mock_json),
                                 headers=headers)
        return response

    def testCreateClient(self) -> None:
        """
        Create a new client
        """
        mock_json = {'first_name': 'foo',
                     'last_name': 'bar',
                     'email': 'foo@bar',
                     'phone': '1234567890',
                    }
        response = self.put_client(mock_json)
        self.assertEqual(response.status_code, 200)


    def testGetClient(self) -> None:
        """
        Get a client
        """
        response = self.get_client(1)
        self.assertEqual(response.status_code, 200)


    def testDeleteClient(self) -> None:
        """
        Delete a client
        """
        response = self.delete_client(1)
        self.assertEqual(response.status_code, 200)


    def testUpdateClient(self) -> None:
        """
        Update a client
        """
        mock_json = {'first_name': 'foo',
                     'last_name': 'bar',
                     'email': 'foo@bar',
                     'phone': '1234567890',
                    }
        response = self.update_client(1, mock_json)
        self.assertEqual(response.status_code, 200)
