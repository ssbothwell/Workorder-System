import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Generate Flask instance
app = Flask(__name__)

# Load settings from config.py
app.config.from_object(os.environ['APP_SETTINGS'])

# Create SQLAlchemy instance
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import models

@app.route('/projects/new', methods=['POST'])
def new_project():
    return "foobar"


@app.route('/projects', methods=['POST'])
def get_project():
    return "foobar"


@app.route('/projects/delete', methods=['DELETE']
def delete_project():
    return "foobar"


@app.route('/projects/<int:project_id>/update', methods=['POST'])
def update_project():
    return "foobar"


@app.route('/clients', methods=['GET'])
def get_all_clients():
    return "foobar"


@app.route('/clients/<int:client_id>', methods=['GET'])
def get_client():
    return "foobar"


@app.route('/clients/new', methods=['POST'])
def new_client():
    return "foobar"


@app.route('/clients/<int:client_id>/delete', methods=['DELETE'])
def delete_client():
    return "foobar"


@app.route('/clients/<int:client_id>/update', methods=['POST'])
def update_client():
    return "foobar"


if __name__ == '__main__':
    app.run()
