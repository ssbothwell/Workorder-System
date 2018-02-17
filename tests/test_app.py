import os
import sys
sys.path.insert(0,os.path.abspath(__file__+"/.."))

import app

class TestCase(unittest.TestCase):
    """Base test class"""
    self.old_path = os.environ["APP_SETTINGS"]
    def create_app(self):
        self.old_env = os.environ["APP_SETTINGS"]
        #os.environ["APP_SETTINGS"] = "config.TestingConfig"
        return 

    def setUp(self):
        app.db.create_all()

    def tearDown(self):
        app.db.session.remove()
        app.db.drop_all()
        #app.os.environ["APP_SETTINGS"] = self.old_env

    def testFoo(self):
        pass
        
