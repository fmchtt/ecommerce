from api.models.user_model import User
from sqlalchemy.orm import Session
from api.services import auth

def get_user_by_email(email: str, db: Session):
  return db.query(User).filter(User.email == email).first()

def registration(email: str, username: str, password: str, db: Session):
  user_new = User(email=email, username=username, hashed_password=auth.hash_password(password))
  db.add(user_new)
  db.commit()
  db.refresh(user_new)
  return user_new

def buscar_me(id, db: Session):
  return db.query(User).filter(User.id == id).first()