"""
Fabco Work Order System Controllers
Solomon Bothwell
ssbothwell@gmail.com
"""
import os
from datetime import datetime
from decimal import Decimal
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
        p_dict = project_schema.validate(request.get_json())
        p_dict = gen_datetimes(p_dict)
        p_dict = gen_total(p_dict)
        line_items = p_dict.pop('line_items', None)
    except:
        return jsonify({'msg': 'Incorrect JSON Schema'}), 400

    try:
        _ = Client.query.filter(Client.id == p_dict['client_id']).one()
    except:
        return jsonify({'msg': 'No Such User'}), 400


    project = Project(**p_dict)
    db.session.add(project)
    create_lineitems(project, line_items)
    db.session.commit()

    return jsonify({'msg': 'Project Added'}), 200


@app.route('/projects', methods=['GET'])
def get_all_projects():
    """ return a list of all projects """
    projects = Project.query.all()
    results = [p.get_dict() for p in projects]
    return jsonify(results), 200


@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """ return a single project by id """
    project = Project.query.filter(Project.id == project_id).one_or_none()
    if project:
        return jsonify(project.get_dict()), 200
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
    try:
        p_dict = project_schema.validate(request.get_json())
        p_dict = gen_total(p_dict)
        p_dict = gen_datetimes(p_dict)
        line_items = validated.pop('line_items', None)
    except:
        return jsonify({'msg': 'Incorrect JSON Schema'}), 400

    try:
        _ = Client.query.filter(Client.id == p_dict['client_id']).one()
    except:
        return jsonify({'msg': 'No Such User'}), 400

    project = Project.query.filter(Project.id == 
                                   project_id).one_or_none()
    if project:

        project = Project(**p_dict)
        db.session.add(project)
        create_lineitems(project, line_items)
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


def create_lineitems(project, line_items) -> None:
    """ Create lineitems from request dict """
    delete_all_lineitems(project)

    for item in line_items:
        if item['p_type'] == 'strainer_bar':
            model = Strainer_Bar(
                project_id=project.id,
                p_type=item['p_type'],
                width=item['width'],
                height=item['height'],
                thickness=item['thickness'],
                price=item['price'],
                quantity=item['quantity'],
                total=item['total'],
                notes=item['notes'])

        if item['p_type'] == 'panel':
            model = Panel(
                project_id=project.id,
                p_type=item['p_type'],
                width=item['width'],
                height=item['height'],
                thickness=item['thickness'],
                price=item['price'],
                quantity=item['quantity'],
                total=item['total'],
                notes=item['notes'])

        if item['p_type'] == 'pedestal':
            model = Pedestal(
                project_id=project.id,
                p_type=item['p_type'],
                width=item['width'],
                height=item['height'],
                depth=item['depth'],
                price=item['price'],
                quantity=item['quantity'],
                total=item['total'],
                notes=item['notes'])

        if item['p_type'] == 'custom_project':
            item = Custom_Project(
                project_id=project.id,
                p_type=item['p_type'],
                price=item['price'],
                quantity=item['quantity'],
                total=item['total'],
                notes=item['notes'])

        db.session.add(item)
    return


def gen_datetimes(_dict: dict) -> dict:
    """ replace date ISO8061 date strings with
    datetime objects in a dict """
    strptime = datetime.strptime
    _dict['due_date'] = strptime(_dict['due_date'], '%Y-%m-%d')
    _dict['completion_date'] = strptime(_dict['completion_date'], '%Y-%m-%d'),
    return _dict


def gen_total(_dict: dict) -> dict:
    """ Tallys the project total from line_items """
    total = Decimal('0')
    for item in _dict['line_items']:
        total += (Decimal(str(item['price'])) *
                  Decimal(str(item['quantity'])))
    _dict['total'] = total
    return _dict


if __name__ == '__main__':
    app.run()
