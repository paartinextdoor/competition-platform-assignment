from App.models import User, Student, Host
from App.database import db
from sqlalchemy.exc import SQLAlchemyError

def create_user(username, password, type="student"):
    try: 
        if type.lower()=="student":
            newuser = Student(username=username, password=password)
        elif type.lower()=="host":
            newuser = Host(username=username, password=password)
        else:
            print("Error: invalid user type!")
            return None
        db.session.add(newuser)
        db.session.commit()
        return newuser
    except SQLAlchemyError as e:
            db.session.rollback()
            print(f'Error:{e}')
            return None

def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        print(f"User: {id} deleted")
        return user
    else:
        print("User not found!")
        return None 


def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None