from App.database import db

class Result(db.Model):
    __tablename__ = 'result'
    resultID = db.Column(db.Integer, primary_key=True)
    fileID = db.Column(db.Integer, db.ForeignKey('resultsFile.fileID'), nullable=False)
    studentID = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    score = db.Column(db.Float)
    rank = db.Column(db.Integer)

def __init__(self, studentID, fileID, score):
    self.studentID = studentID
    self.fileID = fileID
    self.score = score
    self.rank = 0

def __repr__(self):
        return f' <Result {self.compID} - {self.id} - {self.score} - {self.rank} '