from flask import Flask, render_template
from db import barcha_kafedralar, barcha_professorlar, barcha_talabalar

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def test():
    ism = ["Sardor", "Tohir", "Jahongir"]
    return render_template("test1.html", ism=ism)

if __name__ == "__main__":
    app.run(debug=True)