"""
Fabco Work Order System Controllers
Solomon Bothwell
ssbothwell@gmail.com
"""
import os
from datetime import datetime
from flask import Flask, request, jsonify
from models import (db, Project, Client, Strainer_Bar,
                    Panel, Pedestal, Custom_Project)
from validators import client_schema, project_schema

# Generate Flask instance
app = Flask(__name__)

# Set deployment context from environment variable
app.config.from_object(os.environ['APP_SETTINGS'])

# Create SQLAlchemy instance
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/projects/new', methods=['POST'])
def new_project():
    """ Add a project to a database """
    try:
        validated = project_schema.validate(request.get_json())
    except KeyError:
        return jsonify({'msg': 'Incorrect JSON Schema'}), 400

    # Must ensure client_id is for a real client
    client_id = validated['client_id']
    # Convert date strings to datetime objects
    due_date = validated['due_date']
    completion_date = validated['completion_date']
    project_title = validated['project_title']
    status = validated['status']
    deposit = validated['deposit']
    discount = validated['discount']

    project = Project(client_id=client_id,
                      due_date=datetime.strptime(due_date, '%m-%d-%Y'),
                      completion_date=datetime.strptime(completion_date, '%m-%d-%Y'), 
                      project_title=project_title,
                      status=status,
                      deposit=deposit,
                      discount=discount)
    db.session.add(project)
    update_lineitems(project)
    db.session.commit()

    return jsonify({'msg': 'User Added'}), 200


@app.route('/projects', methods=['GET'])
def get_all_projects():
    """ return a list of all projects """
    projects = Project.query.all()

    results = [{"id": project.id,
                "client_id": project.client_id,
                "create_date": project.create_date,
                "due_date": project.due_date,
                "completion_date": project.completion_date,
                "project_title": project.project_title,
                "status": project.status,
                "deposit": str(project.deposit),
                "discount": str(project.discount),
                "line_items": (project.strainer_bars +
                               project.panels +
                               project.pedestals +
                               project.custom_projects)
               } for project in projects]
    return jsonify(results), 200


@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """ return a single project by id """
    project = Project.query.filter(Project.id == project_id).one_or_none()

    if project:
        result = {"id": project.id,
                  "client_id": project.client_id,
                  "create_date": project.create_date,
                  "due_date": project.due_date,
                  "completion_date": project.completion_date,
                  "project_title": project.project_title,
                  "status": project.status,
                  "deposit": str(project.deposit),
                  "discount": str(project.discount),
                  "line_items": (project.strainer_bars +
                                 project.panels +
                                 project.pedestals +
                                 project.custom_projects)
                 }
        return jsonify(result), 200
    return jsonify({'msg': 'No Such Project'}), 400


@app.route('/projects/<int:project_id>/delete', methods=['DELETE'])
def delete_project(project_id):
    """ Remove a project from the database """
    project = Project.query.filter(Project.id == project_id).one_or_none()
    if project:
        db.session.delete(project)
        db.session.commit()
        return jsonify({'msg': 'Project deleted'}), 200
    return jsonify({'msg': 'No Such Project'}), 400


@app.route('/projects/<int:project_id>/update', methods=['POST'])
def update_project(project_id):
    """ Updates all fields on a project with request """
    project = Project.query.filter(Project.id == project_id).one_or_none()

    try:
        validated = project_schema.validate(request.get_json())
    except KeyError:
        return jsonify({'msg': 'Incorrect JSON Schema'}), 400

    if project:
        project.client_id = validated['client_id']
        project.due_date = validated['due_date']
        project.completion_date = validated['completion_date']
        project.project_title = validated['project_title']
        project.status = validated['status']
        project.deposit = validated['deposit']
        project.discount = validated['discount']
        update_lineitems(project)

        db.session.commit()
        return jsonify({'msg': 'Project Updated'}), 200
    return jsonify({'msg': 'No Such Project'}), 400


@app.route('/clients', methods=['GET'])
def get_all_clients():
    """ return a list of all clients """
    clients = Client.query.all()
    results = [{"first name": c.first_name,
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
    client = Client.query.filter(Client.id == client_id).one_or_none()

    if client:
        result = {"first_name" : client.first_name,
                  "last_name" : client.last_name,
                  "email" : client.email,
                  "phone" : client.phone
                 }
        return jsonify(result), 200
    return jsonify({'msg': 'no such user'}), 400


@app.route('/clients/<int:client_id>/projects', methods=['GET'])
def get_client_projects(client_id):
    """ return all projects belonging to client """
    client = Client.query.filter(Client.id == client_id).one_or_none()

    if client:
        result = [{"project_title": p.project_title,
                   "due_date": p.due_date,
                   "status": p.status
                  } for p in client.projects
                 ]
        return jsonify(result), 200
    return jsonify({'msg': 'No Such User'}), 400


@app.route('/clients/new', methods=['POST'])
def new_client():
    """ Add a client to a database """
    try:
        validated = client_schema.validate(request.get_json())
    except KeyError:
        return jsonify({'msg': 'Incorrect JSON Schema'}), 400

    first_name = validated['first_name']
    last_name = validated['last_name']
    email = validated['email']
    phone = validated['phone']

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
    client = Client.query.filter(Client.id == client_id).one_or_none()
    if client:
        db.session.delete(client)
        db.session.commit()
        return jsonify({'msg': 'User deleted'}), 200
    return jsonify({'msg': 'No Such User'}), 400


@app.route('/clients/<int:client_id>/update', methods=['POST'])
def update_client(client_id):
    """ Update a client's details """
    try:
        validated = client_schema.validate(request.get_json())
    except KeyError:
        return jsonify({'msg': 'Incorrect JSON Schema'}), 400

    client = Client.query.filter(Client.id == client_id).one_or_none()

    if client:
        client.first_name = validated['first_name']
        client.last_name = validated['last_name']
        client.email = validated['email']
        client.phone = validated['phone']
        db.session.commit()
        return jsonify({'msg': 'User Updated'}), 200
    return jsonify({'msg': 'No Such User'}), 400


def delete_all_lineitems(project) -> None:
    """ Delete all project line items """
    strainers = Strainer_Bar.query.filter(Strainer_Bar.project_id == project.id).all()
    panels = Panel.query.filter(Panel.project_id == project.id).all()
    pedestals = Pedestal.query.filter(Pedestal.project_id == project.id).all()
    custom_projects = Custom_Project.query.filter(Custom_Project.project_id == project.id).all()

    for item in strainers + panels + pedestals + custom_projects:
        db.session.delete(item)
    return


def update_lineitems(project) -> None:
    """ Update lineitems from request """
    delete_all_lineitems(project)

    for s in request.get_json()['strainer_bars']:
        Strainer_Bar(
            project_id=project.id,
            width=s['width'],
            height=s['height'],
            thickness=s['thickness'],
            price=s['price'],
            quantity=s['quantity'],
            total=s['total'],
            notes=s['notes'])
        db.session.add(s)

    for p in request.get_json()['panels']:
        Panel(
            project_id=project.id,
            width=p['width'],
            height=p['height'],
            thickness=p['thickness'],
            price=p['price'],
            quantity=p['quantity'],
            total=p['total'],
            notes=p['notes'])
        db.session.add(p)

    for p in request.get_json()['pedestals']:
        Pedestal(
            project_id=project.id,
            width=p['width'],
            height=p['height'],
            depth=p['depth'],
            price=p['price'],
            quantity=p['quantity'],
            total=p['total'],
            notes=p['notes'])
        db.session.add(p)

    for p in request.get_json()['custom_projects']:
        Custom_Project(
            project_id=project.id,
            price=p['price'],
            quantity=p['quantity'],
            total=p['total'],
            notes=p['notes'])
        db.session.add(p)

    return

if __name__ == '__main__':
    app.run()
