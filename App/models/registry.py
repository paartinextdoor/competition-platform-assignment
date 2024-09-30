from App.database import db

class Registry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    compID = db.Column(db.Integer, db.ForeignKey('competition.compID'), nullable=False)
    studentID = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

    def __init__(self, studentID, compID):
        self.studentID = studentID
        self.compID = compID
    