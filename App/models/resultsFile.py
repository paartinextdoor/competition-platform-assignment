from App.database import db

class ResultsFile(db.Model):
    __tablename__ = 'resultsFile'
    fileID = db.Column(db.Integer, primary_key=True)
    compID = db.Column(db.Integer, db.ForeignKey('competition.compID'), nullable=False)
    results =  db.relationship('Result', backref='resultsFile', lazy=True, cascade="all, delete-orphan")

    def __init__(self, compID):
        self.compID = compID
        