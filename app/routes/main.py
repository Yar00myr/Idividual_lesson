import os
import json
from flask import render_template
from .. import app

def students_data():
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, '..', 'students_mark.json')
    
    with open(json_path, "r", encoding='utf-8') as student_mark:
        students_mark = json.load(student_mark)
    return students_mark["students"]

@app.route('/')
def index():
    students_mark = students_data()
    return render_template("students.html", students_mark_=students_mark)
