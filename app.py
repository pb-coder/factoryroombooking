from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)