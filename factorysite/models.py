from factorysite import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

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