from fastapi import APIRouter, Depends
from api.services.auth import login
from api.schemas.auth import Login
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from api.database import SessionLocal
from fastapi_jwt_auth import AuthJWT
from datetime import timedelta

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

auth_routes = APIRouter()

@auth_routes.post("/login/", response_model=Login)
def logar(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
  return login(user.username, user.password, db, Authorize)

@auth_routes.post("/logout/", response_model=Login)
def deslogar(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    Authorize.unset_jwt_cookies()
    return {"detail":"Deslogado com sucesso!"}

@auth_routes.post("/refresh/", response_model=Login)
def recarregar_token(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()

    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user, expires_time=timedelta(days=1))
    # Set the JWT cookies in the response
    Authorize.set_access_cookies(new_access_token)

    return {"detail":"Token recarregado com sucesso!"}
