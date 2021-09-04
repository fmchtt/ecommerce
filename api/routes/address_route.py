from typing import List
from fastapi import APIRouter, Depends, Request
from fastapi_jwt_auth import AuthJWT
from api.database import SessionLocal
from sqlalchemy.orm import Session
from api.controllers import address_controller
from api.schemas import adress

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

routes = APIRouter(prefix="/address")

@routes.get("/", response_model=List[adress.Address])
def listar_enderecos(Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
  Authorize.jwt_required()
  return address_controller.listar_endereços(db, Authorize.get_jwt_subject())

@routes.post("/", response_model=List[adress.Address])
def adicionar_endereco(address: adress.AddressCreate, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
  Authorize.jwt_required()
  return address_controller.adicionar_endereco(db, Authorize.get_jwt_subject(), address)

@routes.delete("/{address_id}/", response_model=List[adress.Address])
def remover_endereco(address_id: int, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
  Authorize.jwt_required()
  return address_controller.deletar_endereco(db, Authorize.get_jwt_subject(), address_id)