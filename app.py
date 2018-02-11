import os
from flask import Flask, request, jsonify
from models import db, Project, Client

# Generate Flask instance
app = Flask(__name__)

# Set deployment context from environment variable
app.config.from_object(os.environ['APP_SETTINGS'])

# Create SQLAlchemy instance
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/projects/new', methods=['POST'])
def new_project():
    return "foobar"


@app.route('/projects', methods=['GET'])
def get_all_projects():
    """ return a lits of all projects """
    projects = Project.query.all()
    return jsonify(projects), 200


@app.route('/projects/delete', methods=['DELETE'])
def delete_project():
    return "foobar"


@app.route('/projects/<int:project_id>/update', methods=['POST'])
def update_project():
    return "foobar"


@app.route('/clients', methods=['GET'])
def get_all_clients():
    """ return a list of all clients """
    clients = Client.query.all()
    results = [ { "first name": c.first_name,
                  "last_name" : c.last_name,
                  "email" : c.email,
                  "phone" : c.phone,
                  "id" : c.id,
                } for c in clients
              ]

    return jsonify(results), 200


@app.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    """ return a client by ID """
    client = Client.query.filter(Client.id==client_id).one_or_none()
    
    if client:
        result = { "first_name" : client.first_name,
                   "last_name" : client.last_name,
                   "email" : client.email,
                   "phone" : client.phone
                 }
        return jsonify(result), 200
    return jsonify({'msg': 'no such user'}), 400


@app.route('/clients/<int:client_id>/projects', methods=['GET'])
def get_client_projects(client_id):
    """ return all projects belonging to client """
    client = Client.query.filter(Client.id==client_id).one_or_none()

    if client:
        result = [ {"project_title": p.project_title,
                    "due_date": p.due_date,
                    "status": p.status
                   } for p in client.projects
                 ]
        return jsonify(result), 200
    return jsonify([]), 200


@app.route('/clients/new', methods=['POST'])
def new_client():
    """ Add a client to a database """
    first_name = request.get_json()['first_name']
    last_name = request.get_json()['last_name']
    email = request.get_json()['email']
    phone = request.get_json()['phone']
    
    client = Client(first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone)
    db.session.add(client)
    db.session.commit()

    return jsonify({'msg': 'User Added'}), 200


@app.route('/clients/<int:client_id>/delete', methods=['DELETE'])
def delete_client(client_id):
    """ Remove a client from the database """
    client = Client.query.filter(Client.id==client_id).one_or_none()
    if client:
        db.session.delete(client)
        db.session.commit()
        return jsonify({'msg': 'User deleted'}), 200
    return jsonify({'msg': 'No Such User'}), 400


@app.route('/clients/<int:client_id>/update', methods=['POST'])
def update_client(client_id):
    """ Update a client's details """
    client = Client.query.filter(Client.id==client_id).one_or_none()
    
    if client:
        client.first_name = request.get_json()['first_name']
        client.last_name = request.get_json()['last_name']
        client.email = request.get_json()['email']
        client.phone = request.get_json()['phone']
        db.session.commit()
        return jsonify({'msg': 'User updated'}), 200
    return jsonify({'msg': 'no such user'}), 400


if __name__ == '__main__':
    app.run()
