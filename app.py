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
    """ Add a project to a database """
    client_id = request.get_json()['client_id']
    create_date = request.get_json()['create_date']
    due_date = request.get_json()['due_date']
    completion_date = request.get_json()['completion_date']
    project_title = request.get_json()['project_title']
    status = request.get_json()['status']
    deposit = request.get_json()['deposit']
    discount = request.get_json()['discount']

    project = Project(client_id=client_id,
                      create_date=create_date,
                      due_date=due_date,
                      completion_date=completion_date,
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
    
    result = [ { "id": project.id,
               "client_id": project.client_id,
               "create_date": project.create_date,
               "due_date": project.due_date,
               "completion_date": project.completion_date,
               "project_title": project.project_title,
               "status": project.status,
               "deposit": project.deposit,
               "discount": project.discount,
               "line_items": (project.strainer_bars +
                              project.panels +
                              project.pedestals +
                              project.custom_projects)
             } for project in projects ]
    return jsonify(projects), 200


@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """ return a single project by id """
    project = Project.query.filter(Project.id==project_id).one_or_none()
    
    if project:
        result = { "id": project.id,
                   "client_id": project.client_id,
                   "create_date": project.create_date,
                   "due_date": project.due_date,
                   "completion_date": project.completion_date,
                   "project_title": project.project_title,
                   "status": project.status,
                   "deposit": project.deposit,
                   "discount": project.discount,
                   "line_items": (project.strainer_bars +
                                  project.panels +
                                  project.pedestals +
                                  project.custom_projects)
                 }
        return jsonify(result), 200
    return jsonify({'msg': 'No Such Project'}), 400


@app.route('/projects/delete', methods=['DELETE'])
def delete_project():
    """ Remove a project from the database """
    project = Project.query.filter(Project.id==project_id).one_or_none()
    if project:
        db.session.delete(project)
        db.session.commit()
        return jsonify({'msg': 'Project deleted'}), 200
    return jsonify({'msg': 'No Such Project'}), 400


@app.route('/projects/<int:project_id>/update', methods=['POST'])
def update_project(project_id):
    project = Project.query.filter(Project.id==project_id).one_or_none()

    if project:
        project.client_id = request.get_json()['client_id']
        project.create_date = request.get_json()['create_date']
        project.due_date = request.get_json()['due_date']
        project.completion_date = request.get_json()['completion_date']
        project.project_title = request.get_json()['project_title']
        project.status = request.get_json()['status']
        project.deposit = request.get_json()['deposit']
        project.discount = request.get_json()['discount']
        update_lineitems(project)

        db.session.commit()
        return jsonify({'msg': 'Project Updated'}), 200
    return jsonify({'msg': 'No Such Project'}), 400

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
    return jsonify({'msg': 'No Such User'}), 400


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
        return jsonify({'msg': 'User Updated'}), 200
    return jsonify({'msg': 'No Such User'}), 400


def delete_all_lineitems(project) -> None:
    """ Delete all project line items """
    strainers = Strainer_Bar.query.filter(Strainer_Bar.project_id==project.id).all()
    panels = Panel.query.filter(Panel.project_id==project.id).all()
    pedestals = Pedestals.query.filter(Pedestals.project_id==project.id).all()
    custom_projects = Custom_Project.query.filter(Custom_Project.project_id==project.id).all()

    for item in strainers + panels + pedestals + custom_projects:
        db.session.delete(item)
    return


def update_lineitems(project) -> None:
    """ Update lineitems from request """
    delete_all_lineitems(project)

    for s in request.get_json()['strainer_bars']:
        Strainer_Bar(
        project_id=project.id
        width=s['width'],
        height=s['height'],
        thickness=s['thickness'],
        price=s['price'],
        notes=s['notes'])
        db.session.add(s)

    for p in request.get_json()['panels']:
        Panel(
        project_id=project.id
        width=p['width'],
        height=p['height'],
        thickness=p['thickness'],
        price=p['price'],
        notes=p['notes'])
        db.session.add(p)

    for p in request.get_json()['pedestals']:
        Pedestal(
        project_id=project.id
        width=p['width'],
        height=p['height'],
        depth=p['depth'],
        price=p['price'],
        notes=p['notes'])
        db.session.add(p)

    for p in request.get_json()['custom_project']:
        Custom_Project(
        project_id=project.id
        price=p['price'],
        notes=p['notes'])
        db.session.add(p)

    return

if __name__ == '__main__':
    app.run()
