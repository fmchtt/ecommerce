from api.models import User
from sqlalchemy.orm import Session
from api.services import auth
from fastapi import UploadFile, HTTPException
from api.services.files import save_file

def get_user_by_email(email: str, db: Session):
  return db.query(User).filter(User.email == email).first()

def registration(email: str, username: str, password: str, db: Session):
  user_new = User(email=email, username=username, hashed_password=auth.hash_password(password))
  db.add(user_new)
  db.commit()
  db.refresh(user_new)
  return user_new

def buscar_me(id, db: Session, url: str):
  user = db.query(User).filter(User.id == id).first()

  if not user:
    raise HTTPException(404, "Usuario nao encontrado")

  user.avatar_url = f"{url}{user.avatar_url}"

  return user

  

def alterar_avatar(db: Session, user_id: int, avatar: UploadFile):
  user = db.query(User).filter(User.id == user_id).first()

  if not user:
    raise HTTPException(404, "Usuario nao encontrado")

  user.avatar_url = save_file(avatar)
  db.commit()
  db.refresh(user)
  return user