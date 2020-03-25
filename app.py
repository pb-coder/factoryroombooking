from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "84a67df87b0aa0bd95caaa4747538413"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

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

rooms = [

    {
        "name" : "HTML",
        "number" : "3.10.7",
        "capacity" : "10 People",
        "equipment" : "TV + ChromeCast",
    },

    {
        "name" : "Swift",
        "number" : "3.10.8",
        "capacity" : "15 People",
        "equipment" : "TV",
    },

]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", rooms=rooms)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "csstag")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "test@test.com" and form.password.data == "password":
            flash("You have been logged in!", "csstag")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check username and password", "csstag")
    return render_template("login.html", title="Login", form=form)

if __name__ == '__main__':
    app.run(debug=True)