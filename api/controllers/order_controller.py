from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import and_
from api.models import Product, User, Order, AssociationOrderProduct, Address
from fastapi import HTTPException

def listar_user_orders(db: Session, user_id: int, url: str):
  orders = db.query(Order).filter(and_(Order.owner_id==user_id, Order.finalized==True)).all()

  for order in orders:
    for association in order.products:
        for image in association.products.images:
          image.path = f"{url}{image.path}"

  return orders

def listar_carrinho(db: Session, user_id: int, url: str):
  user = db.query(User).filter(User.id==user_id).first()

  if not user:
    raise HTTPException(404, "Usuario nao encontrado")

  cart = db.query(Order).filter(and_(Order.owner_id == user.id, Order.finalized == False)).first()

  if not cart:
    raise HTTPException(404, "Carrinho nao encontrado")

  
  for association in cart.products:
      for image in association.products.images:
        image.path = f"{url}{image.path}"

  return cart

def adicionar_produto_carrinho(db: Session, user_id: int, product_id: int, quantity: int, url: str):
  user = db.query(User).filter(User.id==user_id).first()

  if not user:
    raise HTTPException(404, "Usuario nao encontrado")

  cart = db.query(Order).filter(and_(Order.owner_id == user.id, Order.finalized == False)).first()

  if not cart:
    cart = Order(owner_id=user.id)
    db.add(cart)
    db.commit()
    db.refresh(cart)

  produto = db.query(Product).filter(Product.id==product_id).first()

  if not produto:
    raise HTTPException(404, "Produto nao encontrado")

  assoc = db.query(AssociationOrderProduct).filter(and_(AssociationOrderProduct.product_id == produto.id, AssociationOrderProduct.order_id == cart.id)).first()

  if assoc:
    assoc.quantity = quantity
  else:
    assoc = AssociationOrderProduct(product_id=produto.id, order_id=cart.id, quantity=quantity)
    db.add(assoc)

  db.commit()
  db.refresh(cart)

  for association in cart.products:
      for image in association.products.images:
        image.path = f"{url}{image.path}"

  return cart

def remover_produto_carrinho(db: Session, user_id: int, product_id: int, url: str):
  user = db.query(User).filter(User.id==user_id).first()

  if not user:
    raise HTTPException(404, "Usuario nao encontrado")

  cart = db.query(Order).filter(and_(Order.owner_id == user.id, Order.finalized == False)).first()

  if not cart:
    raise HTTPException(404, "Carrinho nao encontrado")

  produto = db.query(Product).filter(Product.id==product_id).first()

  if not produto:
    raise HTTPException(404, "Produto nao encontrado")

  assoc = db.query(AssociationOrderProduct).filter(and_(AssociationOrderProduct.product_id == produto.id, AssociationOrderProduct.order_id == cart.id)).first()

  if not assoc:
    raise HTTPException(404, "Produto nao encontrado no carrinho")

  db.delete(assoc)
  db.commit()
  db.refresh(cart)

  for association in cart.products:
      for image in association.products.images:
        image.path = f"{url}{image.path}"


  return cart

def finalizar_pedido(db: Session, user_id: int, address_id: int, url: str):
  user = db.query(User).filter(User.id==user_id).first()

  if not user:
    raise HTTPException(404, "Usuario nao encontrado")

  address = db.query(Address).filter(and_(Address.id == address_id, Address.user_id == user_id)).first()

  if not address:
    raise HTTPException(404, "Endereco nao encontrado no pefil do usuario")  

  cart = db.query(Order).filter(and_(Order.owner_id == user.id, Order.finalized == False)).first()

  if not cart:
    raise HTTPException(404, "Carrinho nao encontrado")

  cart.finalized = True
  cart.ship_address_id = address.id

  db.commit()
  db.refresh(cart)

  for association in cart.products:
      for image in association.products.images:
        image.path = f"{url}{image.path}"

  return cart