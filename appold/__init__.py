import os
from flask import Flask

### Configuration

# Create application instance and load config
app = Flask(__name__)
app.config.from_object(__name__)


# Default config
# secret keys and database user info MUST be overwritten
# on production server using environment variables
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'trip_test.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('WORKORDER_SETTINGS', silent=True)


### Project Imports
import workorder.database
import workorder.controllers
#import workorder.validators
#import workorder.models
