from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home")
@app.route("/")
@app.route("/lacrosse")
def home():
    return render_template("home.html")


@app.route("/defenders")
def defense():
    return render_template("defense.html")


@app.route("/midfielders")
def middle():
    return render_template("middle.html")


@app.route("/attackers")
def attack():
    return render_template("attack.html")


if __name__ == "__main__":
    app.run(debug=True)
