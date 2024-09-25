import random
from datetime import datetime
from flask import render_template, redirect
from .. import app
from ..helpers import students_data, site_map


def get_background_image():
    current_time = datetime.now()

    if 5 <= current_time.hour < 18:
        return "light_white_bg.jpg"
    else:
        return "dark_bg.jpg"


@app.get("/")
def index():
    # print([x for x in app.url_map.iter_rules() if "GET" in x.methods and has_no_empty_params(x)])

    json_path = "students_mark.json"
    students_mark = students_data(json_path)
    background_image = get_background_image()
    return render_template(
        "students.html",
        students_mark_=students_mark,
        site_map=site_map(),
        bg_image=background_image,
    )


@app.route("/information")
def info():
    return render_template("info.html", site_map=site_map())

@app.route("/register")
def register():
    return render_template("info.html", site_map=site_map())

@app.route("/items/<int:item_id>/details")
def item_details(item_id:int):
    return render_template("info.html", site_map=site_map())

@app.route("/random-endpoint")
def random_endpoint():
    endpoint = random.choice(["/", "/information"])

    return redirect(endpoint)
