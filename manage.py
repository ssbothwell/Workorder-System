import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db

# Get our app environment
app.config.from_object(os.environ['APP_SETTINGS'])


# Create a migrate instance
migrate = Migrate(app, db)

# Create a manager and add the db command to run the migration
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
