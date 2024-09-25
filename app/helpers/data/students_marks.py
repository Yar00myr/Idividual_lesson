import json   

def students_data(json_path):
    
    with open(json_path, "r", encoding='utf-8') as student_mark:
        students_mark = json.load(student_mark)
    return students_mark["students"]
