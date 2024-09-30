from sqlite3 import IntegrityError
from App.models import Competition, Result
from App.database import db

def register_student(compID, studentID):
    student = Competition.query.filter_by(id=studentID, compID=compID).first()
    if student:
        print("Student is already registered!")
        return None
    student = Competition(id=studentID, compID=compID)
    try:
        db.session.add(student)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()    
    return student

def view_student_results(studentID):
    student_results = Result.query.filter_by(id=studentID).first()
    return student_results
