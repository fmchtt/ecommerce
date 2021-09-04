from typing import List
from fastapi import APIRouter, Depends, Request
from fastapi_jwt_auth import AuthJWT
from api.database import SessionLocal
from sqlalchemy.orm import Session
from api.controllers import order_controller
from api.schemas import Order

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

routes = APIRouter(prefix="/order")

@routes.get("/", response_model=List[Order])
def listar_pedidos_usuario(request: Request, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
  Authorize.jwt_required()
  return order_controller.listar_user_orders(db, Authorize.get_jwt_subject(), request.base_url)

@routes.get("/cart/", response_model=Order)
def mostrar_carrinho(request: Request, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    Authorize.jwt_required()
    return order_controller.listar_carrinho(db, Authorize.get_jwt_subject(), request.base_url)

@routes.post("/cart/{product_id}/quantity/{quantity}/", response_model=Order)
def adicionar_carrinho(request: Request, product_id: int, quantity: int, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    Authorize.jwt_required()
    return order_controller.adicionar_produto_carrinho(db, Authorize.get_jwt_subject(), product_id, quantity, request.base_url)

@routes.post("/cart/finalize/{address_id}/", response_model=Order)
def finalizar_pedido(request: Request, address_id: int, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    Authorize.jwt_required()
    return order_controller.finalizar_pedido(db, Authorize.get_jwt_subject(), address_id, request.base_url)

@routes.delete("/cart/{product_id}/", response_model=Order)
def remover_carrinho(request: Request, product_id: int, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    Authorize.jwt_required()
    return order_controller.remover_produto_carrinho(db, Authorize.get_jwt_subject(), product_id, request.base_url)