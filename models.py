"""
SQLAlchemy ORM Models
"""
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy Instance
db = SQLAlchemy()

class Custom_Project(db.Model):
    __tablename__ = 'custom_projects'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    total = db.Column(db.Numeric, nullable=False)
    notes = db.Column(db.String(), nullable=True)
    p_type = db.Column(db.String(), nullable=False)


    def get_dict(self):
        """ Returns columns as a dictionary """
        return {"id": self.id,
                "p_type": 'custom_project',
                "project_id": self.project_id,
                "quantity": self.quantity,
                "price": str(self.price),
                "total": str(self.total),
                "notes": self.notes
               }


class Pedestal(db.Model):
    __tablename__ = 'pedestals'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    width = db.Column(db.Numeric, nullable=False)
    height = db.Column(db.Numeric, nullable=False)
    depth = db.Column(db.Numeric, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    total = db.Column(db.Numeric, nullable=False)
    notes = db.Column(db.String(), nullable=True)
    p_type = db.Column(db.String(), nullable=False)


    def get_dict(self):
        """ Returns columns as a dictionary """
        return {"id": self.id,
                "p_p_type": "pedestal",
                "project_id": self.project_id,
                "height": str(self.height),
                "width": str(self.width),
                "depth": str(self.depth),
                "quantity": self.quantity,
                "price": str(self.price),
                "total": str(self.total),
                "notes": self.notes
               }


class Panel(db.Model):
    __tablename__ = 'panels'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    width = db.Column(db.Numeric, nullable=False)
    height = db.Column(db.Numeric, nullable=False)
    thickness = db.Column(db.Numeric, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    total = db.Column(db.Numeric, nullable=False)
    notes = db.Column(db.String(), nullable=True)
    p_type = db.Column(db.String(), nullable=False)


    def get_dict(self):
        """ Returns columns as a dictionary """
        return {"id": self.id,
                "p_type": "panel",
                "project_id": self.project_id,
                "height": str(self.height),
                "width": str(self.width),
                "thickness": str(self.thickness),
                "quantity": self.quantity,
                "price": str(self.price),
                "total": str(self.total),
                "notes": self.notes
               }


class Strainer_Bar(db.Model):
    __tablename__ = 'strainer_bars'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    width = db.Column(db.Numeric, nullable=False)
    height = db.Column(db.Numeric, nullable=False)
    thickness = db.Column(db.Numeric, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    total = db.Column(db.Numeric, nullable=False)
    notes = db.Column(db.String(), nullable=True)
    p_type = db.Column(db.String(), nullable=False)

    def get_dict(self):
        """ Returns columns as a dictionary """
        return {"id": self.id,
                "p_type": "strainer_bar",
                "project_id": self.project_id,
                "height": str(self.height),
                "width": str(self.width),
                "thickness": str(self.thickness),
                "quantity": self.quantity,
                "price": str(self.price),
                "total": str(self.total),
                "notes": self.notes
               }


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    create_date = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    due_date = db.Column(db.DateTime(timezone=True))
    completion_date = db.Column(db.DateTime(timezone=True))
    project_title = db.Column(db.String(), nullable=False)
    status = db.Column(db.Integer, default=0)
    deposit = db.Column(db.Numeric, default=0)
    discount = db.Column(db.Numeric, default=0.0)
    total = db.Column(db.Numeric, default=0.0)
    
    strainer_bars = db.relationship('Strainer_Bar') 
    panels = db.relationship('Panel') 
    pedestals = db.relationship('Pedestal') 
    custom_projects = db.relationship('Custom_Project')


    def __init__(self, client_id, due_date, 
                 completion_date, project_title,
                 status, deposit, discount, total):
        self.client_id = client_id
        self.due_date = due_date
        self.completion_date = completion_date
        self.project_title = project_title
        self.status = status
        self.deposit = deposit
        self.discount = discount
        self.total = total


    def get_dict(self) -> dict:
        """ Returns columns as a dictionary """
        return {"id": self.id,
                "client_id": self.client_id,
                "create_date": self.create_date,
                "due_date": self.due_date,
                "completion_date": self.completion_date,
                "self_title": self.project_title,
                "status": self.status,
                "deposit": str(self.deposit),
                "discount": str(self.discount),
                "line_items": self.get_lineitems()
               }


    def get_lineitems(self) -> dict:
        """ returns a dictionary of all lineitems """
        items = (self.strainer_bars +
                 self.panels +
                 self.pedestals +
                 self.custom_projects)
        return [item.get_dict() for item in items]
        


class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(), nullable=True)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=True)
    projects = db.relationship("Project") 

    def __init__(self, first_name,
                 last_name, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def __repr__(self):
        return '<user_id {}>'.format(self.user_id)

