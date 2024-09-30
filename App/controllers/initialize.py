from .user import create_user
from .host import create_comp
from App.database import db
from .competition import add_participant, get_results_file
from .result import add_results
from datetime import datetime
from .data import *


def initialize():
    db.drop_all()
    db.create_all()
    
    # Adding hosts
    for username, password, usertype in hosts:
        create_user(username, password, usertype)

    # Adding students
    for username, password, usertype in students:
        create_user(username, password, usertype)

    # Adding competitions
    for hostID, compName, description, date in competitions:
        create_comp(hostID, compName, description, datetime.strptime(date, "%Y-%m-%d").date())

    # Adding participants
    for studentID, compID in participants:
        add_participant(studentID, compID)

    # Adding results
    for studentID, compID, score in results:
        add_results(studentID, get_results_file(compID).fileID, score)

        