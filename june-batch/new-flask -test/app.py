# pip install flask

from flask import Flask, render_template, request, redirect, flash
import mysql.connector
import os

conn = mysql.connector.connect(host="localhost", username= "root", password="1234", database="flasktable")

curser = conn.cursor()

app = Flask(__name__)
app.secret_key = "sjkdfsjdfbjf"

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

        img = request.files.get("image")
        if img:
            img.save(os.path.join("images", img.filename))
            image_path = os.path.join("images", img.filename)
        else:
            image_data = None
        print(name, number, email, dec)
        # curser.execute(f"insert into flasktables values('','{name}', {number},'{email}', '{dec}', '{image_path}')")
        
        # curser.execute("""
        #     INSERT INTO flasktables (name, phone_number, email, message, image_path)
        #     VALUES (%s, %s, %s, %s, %s)
        # """, (name, number, email, dec, image_path))
        # conn.commit()
        flash("Your data asaved suvessfully.....")
        return redirect("/show")
    return "save data"
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/show")
def show():
    curser.execute("select * from flasktables")
    data = curser.fetchall()
    return render_template("show.html", mydata = data)

@app.route("/delete/<xyz>", methods = ["POST",])
def deletethis(xyz):
    if request.method == "POST":
        curser.execute(f"delete from flasktables where Name = '{xyz}'")
        return redirect("/show")



@app.route("/update/<rt>", methods = ["POST", ])
def updatethis(rt):
    curser.execute(f"select * from flasktables where Name = '{rt}'")
    zx = curser.fetchone()
    return render_template("updateview.html", abc = zx)


@app.route("/updatethis/<t>", methods = ["POST", ])
def updatenow(t):
    if request.method == "POST":
        name = request.form.get("name")
        number = request.form.get("number")
        email = request.form.get("email")
        dec = request.form.get("dec")

        curser.execute(f"update flasktables set Name = '{name}',Phone_Number = {number}, Email = '{email}', Message = '{dec}' where Name = '{t}'")
        conn.commit()
        return redirect("/show")

if __name__ == "__main__":
    app.run(debug = True, port = 1000)
