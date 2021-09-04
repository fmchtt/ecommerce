from sqlalchemy.orm import Session
from api.models import User, Address
from fastapi import HTTPException
from api.schemas import adress

def listar_endereços(db: Session, user_id: int):
  user = db.query(User).filter(User.id==user_id).first()

  if not user:
    raise HTTPException(404, "Usuario nao encontrado")

  return user.addresses

def adicionar_endereco(db: Session, user_id: int, address: adress.AddressCreate):
  user = db.query(User).filter(User.id==user_id).first()

  if not user:
    raise HTTPException(404, "Usuario nao encontrado")

  user.addresses.append(Address(**address.dict()))
  db.commit()
  db.refresh(user)

  return user.addresses


def deletar_endereco(db: Session, user_id: int, address_id: int):
  user = db.query(User).filter(User.id==user_id).first()

  if not user:
    raise HTTPException(404, "Usuario nao encontrado")

  address = db.query(Address).filter(Address.id==address_id).first()

  if not address:
    raise HTTPException(404, "Endereco nao encontrado")

  user.addresses.remove(address)
  db.commit()
  db.refresh(user)

  return user.addresses