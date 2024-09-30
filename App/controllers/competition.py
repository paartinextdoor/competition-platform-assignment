from sqlite3 import IntegrityError
from App.models import Student, Competition, ResultsFile, Result, Registry
from App.database import db


def add_participant(studentID, compID):
    existing_registry = Registry.query.filter_by(studentID=studentID, compID=compID).first()
    if existing_registry:
        print("Student is a participant!")
        return None
    try:
        new_participant = Registry(studentID=studentID, compID=compID)
        db.session.add(new_participant)
        db.session.commit()
        print(f'Student: {studentID} registered for Competition: {compID}')
        return new_participant
    except IntegrityError as e:
        db.session.rollback()    
        return None
    
def remove_participant(registryID):
    existing_registry = Registry.query.get(registryID)
    if existing_registry:
        db.session.delete(existing_registry)
        db.session.commit()
        print("Participant removed!")
        return existing_registry
    else:
        print("Registration not found")
        return None
    
def list_comps():
    comp_list = Competition.query.order_by(Competition.dateOfComp.asc()).all()
    return comp_list

def view_results(compID):
    results_file = ResultsFile.query.filter_by(compID=compID).first()
    results = Result.query.filter_by(fileID=results_file.fileID).all()
    return results

def list_participants(compID):
    participants = Registry.query.filter_by(compID=compID).all()
    return participants

def get_results_file(compID):
    results_file = ResultsFile.query.filter_by(compID=compID).first()
    return results_file