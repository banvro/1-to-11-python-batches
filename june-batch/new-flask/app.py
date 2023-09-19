# pip install flask

from flask import Flask, render_template, request
import mysql.connector


conn = mysql.connector.connect(host="localhost", username= "root", password="1234", database="flasktable")

curser = conn.cursor()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/savedata", methods = ["post"])
def savedata():
    if request.method == "POST":
        name = request.form.get("name")
        number = request.form.get("number")
        email = request.form.get("email")
        dec = request.form.get("dec")

        # print(name, number, email, dec)
        curser.execute(f"insert into flasktable values('{name}', {number},'{email}', '{dec}')")

        return f"save data {name, number, email, dec}"
    return "save data"
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/show")
def show():
    return render_template("show.html")









if __name__ == "__main__":
    app.run(debug = True, port = 1000)
