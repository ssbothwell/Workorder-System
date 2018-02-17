import unittest
import config
import json
import app

class TestClientControllers(unittest.TestCase):
    """Base test class"""

    def setUp(self):
        self.app = app.create_app(config.DevelopmentConfig)
        self.app.db.create_all()

    def tearDown(self):
        app.db.session.remove()
        app.db.drop_all()

    def testCreateClient(self):
        mock_json = {'first_name': 'foo',
                     'last_name': 'bar',
                     'email': 'foo@bar',
                     'phone': '1234567890',
                    }
        headers = {'content-type': 'application/json'}
        response = self.app.post('/clients/new',
                                 data=json.dumbs(mock_json),
                                 headers=headers)
        print(response)
        
