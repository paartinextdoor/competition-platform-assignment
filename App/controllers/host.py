from sqlite3 import IntegrityError
from App.models import Competition, ResultsFile
from App.database import db
from datetime import date

def create_comp(hostID, compName, description, dateOfComp=date.today()):
    existing_comp = Competition.query.filter_by(compName=compName).first()
    if existing_comp:
        print("Competition name taken!")
        return None
    try:
        new_competition = Competition(hostID=hostID, compName=compName, description=description, dateOfComp=dateOfComp)
        db.session.add(new_competition)
        db.session.commit()
        new_file = ResultsFile(compID=new_competition.compID)
        db.session.add(new_file)
        db.session.commit()
        print(f"{compName} was succesfully created by host: {hostID}.")
        return new_competition 
    except IntegrityError as e:
        db.session.rollback()    
        print(f'Error:{e}')
        return None
    
    
def update_comp(compID, compName=None, description=None, dateOfComp=None):
    comp = Competition.query.get(compID)
    if not comp:
        print(f'{compID} not found!')
        return
    if not(compName is None):
        comp.compName = compName
    if not(dateOfComp is None):
        comp.dateOfComp = dateOfComp
    if not(description is None):
        comp.description = description
    try:
        db.session.add(comp)
        db.session.commit()
        print("Competition updated!")
        return None
    except IntegrityError as e:
        db.session.rollback()
        print(f"Error: {e}")
        return None

def delete_comp(compID):
    comp = Competition.query.get(compID)
    if not comp:
        print(f'Competition: {compID} not found!')
        return
    db.session.delete(comp)
    db.session.commit()
    print(f'{comp.compName} deleted!')
