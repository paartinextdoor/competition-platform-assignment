from App.database import db
from App.models import User


class Host(User):
    __tablename__ = 'host'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    
    competitions = db.relationship('Competition', backref='host', lazy=True, cascade="all, delete-orphan")

    __mapper_args__ = {
        'polymorphic_identity': 'host'  # Identify this class as 'Admin'
    }

    def __init__(self, username, password):
        super().__init__(username, password)
        self.usertype = "Host"
        
    def __repr__(self):
        return f' <Admin {self.username} - {self.id} - {self.password} '

    
        
