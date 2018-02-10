"""
SQLAlchemy ORM Models
"""
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy Instance
db = SQLAlchemy()

class custom_project(db.Model):
    __tablename__ = 'custom_projects'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    notes = db.Column(db.String(), nullable=True)

    def __init__(self, id, project_id, price, notes):
        self.id = id
        self.project_id = project_id
        self.price = price
        self.notes = notes


class pedestal(db.Model):
    __tablename__ = 'pedestals'
    pedestal_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, nullable=False)
    width = db.Column(db.Numeric, nullable=False)
    height = db.Column(db.Numeric, nullable=False)
    depth = db.Column(db.Numeric, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    notes = db.Column(db.String(), nullable=True)

    def __init__(self, pedestal, project_id, width,
                 height, depth, price, notes):
        self.pedestal_id = pedestal_id
        self.project_id = project_id
        self.width = width
        self.height = height
        self.thickness = thickness
        self.price = price
        self.notes = notes


class panel(db.Model):
    __tablename__ = 'panels'
    panel_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, nullable=False)
    width = db.Column(db.Numeric, nullable=False)
    height = db.Column(db.Numeric, nullable=False)
    thickness = db.Column(db.Numeric, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    notes = db.Column(db.String(), nullable=True)

    def __init__(self, panel_id, project_id, width,
                 height, thickness, price, notes):
        self.panel_id = panel_id
        self.project_id = project_id
        self.width = width
        self.height = height
        self.thickness = thickness
        self.price = price
        self.notes = notes


class strainer_bar(db.Model):
    __tablename__ = 'strainer_bars'
    strainer_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, nullable=False)
    width = db.Column(db.Numeric, nullable=False)
    height = db.Column(db.Numeric, nullable=False)
    thickness = db.Column(db.Numeric, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    notes = db.Column(db.String(), nullable=True)

    def __init__(self, strainer_id, project_id, width,
                 height, thickness, price, notes):
        self.strainer_id = strainer_id
        self.project_id = project_id
        self.width = width
        self.height = height
        self.thickness = thickness
        self.price = price
        self.notes = notes


class Project(db.Model):
    __tablename__ = 'projects'

    project_id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    due_date = db.Column(db.DateTime(timezone=True))
    completion_date = db.Column(db.DateTime(timezone=True))
    project_title = db.Column(db.String(), nullable=False)
    status = db.Column(db.Integer, default=0)
    deposit = db.Column(db.Numeric, default=0)
    discount = db.Column(db.Numeric, default=0.0)

    def __init__(self, project_id, client_id, create_date,
                 due_date, completion_date, project_title,
                 status, deposit, discount):
        self.client_id = client_id
        self.create_date = create_date
        self.due_date = due_date
        self.completion_date = completion_date
        self.project_title = project_title
        self.status = status
        self.deposit = deposit
        self.discount = discount


class Client(db.Model):
    __tablename__ = 'clients'
    client_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=True)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=True)

    def __init__(self, client_id, first_name,
                 email, phone):
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password


    def __repr__(self):
        return '<user_id {}>'.format(self.user_id)

