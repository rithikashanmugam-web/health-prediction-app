from flask import Flask, render_template, request, redirect
import sqlite3
import pickle

app = Flask(__name__)

# load trained ML model
with open("models/health_model.pkl", "rb") as file:
    model = pickle.load(file)

DATABASE = "database.db"


# create database table
def create_table():

    conn = sqlite3.connect(DATABASE)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS patients(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            dob TEXT,
            email TEXT,
            glucose REAL,
            haemoglobin REAL,
            cholesterol REAL,
            remarks TEXT
        )
    """)

    conn.commit()
    conn.close()


create_table()


# home page
@app.route("/")
def index():

    conn = sqlite3.connect(DATABASE)

    patients = conn.execute(
        "SELECT * FROM patients"
    ).fetchall()

    conn.close()

    return render_template(
        "index.html",
        patients=patients
    )


# add patient
@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        name = request.form["name"]
        dob = request.form["dob"]
        email = request.form["email"]

        glucose = float(
            request.form["glucose"]
        )

        haemoglobin = float(
            request.form["haemoglobin"]
        )

        cholesterol = float(
            request.form["cholesterol"]
        )

        # AI prediction
        prediction = model.predict([[
            glucose,
            haemoglobin,
            cholesterol
        ]])[0]

        conn = sqlite3.connect(DATABASE)

        conn.execute("""
            INSERT INTO patients(
                name,
                dob,
                email,
                glucose,
                haemoglobin,
                cholesterol,
                remarks
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            name,
            dob,
            email,
            glucose,
            haemoglobin,
            cholesterol,
            prediction
        ))

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add.html")


# edit patient
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    conn = sqlite3.connect(DATABASE)

    if request.method == "POST":

        name = request.form["name"]
        dob = request.form["dob"]
        email = request.form["email"]

        glucose = float(
            request.form["glucose"]
        )

        haemoglobin = float(
            request.form["haemoglobin"]
        )

        cholesterol = float(
            request.form["cholesterol"]
        )

        # predict again after update
        prediction = model.predict([[
            glucose,
            haemoglobin,
            cholesterol
        ]])[0]

        conn.execute("""
            UPDATE patients
            SET
                name=?,
                dob=?,
                email=?,
                glucose=?,
                haemoglobin=?,
                cholesterol=?,
                remarks=?
            WHERE id=?
        """,
        (
            name,
            dob,
            email,
            glucose,
            haemoglobin,
            cholesterol,
            prediction,
            id
        ))

        conn.commit()
        conn.close()

        return redirect("/")

    patient = conn.execute(
        "SELECT * FROM patients WHERE id=?",
        (id,)
    ).fetchone()

    conn.close()

    return render_template(
        "edit.html",
        patient=patient
    )


# delete patient
@app.route("/delete/<int:id>")
def delete(id):

    conn = sqlite3.connect(DATABASE)

    conn.execute(
        "DELETE FROM patients WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")


# run flask
if __name__ == "__main__":
    app.run(debug=True)