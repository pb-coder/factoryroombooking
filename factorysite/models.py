from factorysite import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), unique=True, nullable=False)
    rooms = db.relationship("Room", backref="equipment", lazy=True)

    def __repr__(self):
        return f"Equipment('{self.equipment}')"

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    number = db.Column(db.String(15), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    is_booked = db.Column(db.Boolean, default=False, nullable=False)
    equipment_id= db.Column(db.Integer, db.ForeignKey('equipment.id'))

    def __repr__(self):
        return f"Room('{self.name}', '{self.is_booked}')"