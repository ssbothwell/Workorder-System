import unittest
import config
import json
from app import create_app, db

class TestClientControllers(unittest.TestCase):
    """ Base test class """

    def setUp(self):
        self._app = create_app(config.TestingConfig)
        self._app.app_context().push()
        self.app = self._app.test_client()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def put_client(self, mock_json: dict):
        """
        Helper Function for adding Clients to database
        """
        headers = {'content-type': 'application/json'}
        response = self.app.post('/clients/new',
                                 data=json.dumps(mock_json),
                                 headers=headers)
        return response


    def get_client(self, id: int):
        """
        Helper Function for getting a client from database
        """
        headers = {'content-type': 'application/json'}
        response = self.app.post('/clients/' + id,
                                 data=json.dumps(mock_json),
                                 headers=headers)
        return response


    def testCreateClient(self):
        mock_json = {'first_name': 'foo',
                     'last_name': 'bar',
                     'email': 'foo@bar',
                     'phone': '1234567890',
                    }
        response = self.put_client(mock_json)
        self.assertEqual(response.status_code, 200) 
