from flask import render_template, url_for, flash, redirect
from factorysite import app
from factorysite.forms import RegistrationForm, LoginForm
from factorysite.models import User, Equipment, Room

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
@app.route("/index")
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