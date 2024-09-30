from App.database import db

class Competition(db.Model):
    compID = db.Column(db.Integer, primary_key=True)
    hostID = db.Column(db.Integer, db.ForeignKey('host.id'), nullable=False) 
    compName = db.Column(db.String(80), unique=True, nullable=False)
    dateOfComp = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text, nullable=False)
    participants = db.relationship('Registry', backref='competition', lazy=True, cascade="all, delete-orphan")

    def __init__(self, hostID, compName, description, dateOfComp):
        self.hostID = hostID
        self.compName = compName
        self.dateOfComp = dateOfComp
        self.description = description

    def __repr__(self):
        return f' <Competition {self.compID} - {self.compName} - {self.dateOfComp} - {self.description}'    