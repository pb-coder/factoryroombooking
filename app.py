from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config["SECRET_KEY"] = "84a67df87b0aa0bd95caaa4747538413"
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