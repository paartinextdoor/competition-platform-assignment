from App.database import db
from App.models import User

class Student(User):
    __tablename__ = 'student'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    registry = db.relationship('Registry', backref='student', lazy=True, cascade='all, delete-orphan')

    __mapper_args__ = {
        'polymorphic_identity': 'student'  # Identify this class as 'Student'
    }

    def __init__(self, username, password):
        super().__init__(username, password)
        self.usertype = "student"
  
    def __repr__(self):
        return f' <Student {self.id} - {self.username} - {self.password} '
