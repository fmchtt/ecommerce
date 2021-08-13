from datetime import timedelta
from fastapi import HTTPException, Depends
from fastapi_jwt_auth import AuthJWT
from passlib.context import CryptContext
from api.controllers.user_controller import get_user_by_email
from sqlalchemy.orm import Session

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verify_password(plain_password: str, hashed_password: str):
  return pwd_context.verify(plain_password, hashed_password)

def hash_password(password: str):
  return pwd_context.hash(password)

def login(username: str, password: str, db: Session, Authorize: AuthJWT):
    user = get_user_by_email(username, db)
    if not user:
      raise HTTPException(status_code=404, detail="Usuario nao encontrado!")
    elif not verify_password(password, user.hashed_password):
      raise HTTPException(status_code=401, detail="Senha incorreta!")
    else:
      # Create the tokens and passing to set_access_cookies or set_refresh_cookies
      access_token = Authorize.create_access_token(subject=user.id, expires_time=timedelta(days=1))
      refresh_token = Authorize.create_refresh_token(subject=user.id, expires_time=timedelta(days=7))

      # Set the JWT cookies in the response
      Authorize.set_access_cookies(access_token)
      Authorize.set_refresh_cookies(refresh_token)
      return {"detail":"Logado com sucesso!"}
    