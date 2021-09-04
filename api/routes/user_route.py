from fastapi import APIRouter, Form, Depends
from api.schemas import UserLogin, User
from sqlalchemy.orm import Session
from api.database import SessionLocal
from api.controllers import user_controller
from fastapi import Depends
from fastapi_jwt_auth import AuthJWT

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

user_routes = APIRouter(prefix="/users")

@user_routes.post("/create/", response_model=UserLogin)
def registrar(username: str = Form(...), email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
  return user_controller.registration(email, username, password, db)

@user_routes.get("/me/", response_model=User)
def buscar_meu_usuario(Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
  Authorize.jwt_required()

  user_id = Authorize.get_jwt_subject()
  return user_controller.buscar_me(user_id, db)