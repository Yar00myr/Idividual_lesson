import random
from flask import render_template, redirect
from .. import app
from ..helpers import students_data


@app.route('/')
def index():
    json_path = 'students_mark.json'
    students_mark = students_data(json_path)
    return render_template("students.html", students_mark_=students_mark)


@app.route("/information")
def info():
    return render_template("info.html")


@app.route("/random-endpoint")
def random_endpoint():
    endpoint = random.choice(["/", "/information"])
    return redirect(endpoint)
