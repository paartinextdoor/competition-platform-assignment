from App.models import Result
from App.database import db
from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError

def rank_competition_results(fileID):
    results = Result.query.filter_by(fileID=fileID).order_by(desc(Result.score)).all()
    for index, result in enumerate(results):
        result.rank = index + 1  
        db.session.add(result)  
    db.session.commit()

def view_result_details(resultID):
    results = Result.query.get(resultID)
    return results

def add_results(studentID, fileID, score):
    existing_results = Result.query.filter_by(studentID=studentID, fileID=fileID).first()
    if existing_results:
        print(f"Results already exists for Student {studentID} in File {fileID}")
        return None 
    try:
        results = Result(studentID=studentID, fileID=fileID, score=score)
        db.session.add(results)
        db.session.commit()
        rank_competition_results(fileID=fileID)
        return results
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Error: {e}")
        return None

def update_results(studentID, fileID, score):
    existing_results = Result.query.filter_by(studentID=studentID, fileID=fileID).first()
    if not existing_results:
        print("Results not found")
        return None
    existing_results.score = score
    db.session.add(existing_results)
    db.session.commit()
    rank_competition_results(fileID=fileID)
    print("Results updated!")
    return existing_results
    
    
