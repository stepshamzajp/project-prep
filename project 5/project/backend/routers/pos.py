from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.order import Order
from models.order_item import OrderItem
from models.menu_item import MenuItem
from schemas.order import OrderCreate

router = APIRouter(prefix="/pos", tags=["POS"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/order")
def create_order(order_data: OrderCreate, db: Session = Depends(get_db)):
    total = 0

    for item in order_data.items:
        menu_item = db.query(MenuItem).filter(MenuItem.id == item.item_id).first()
        total += float(menu_item.price) * item.quantity

    new_order = Order(total_price=total)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    for item in order_data.items:
        order_item = OrderItem(
            order_id=new_order.id,
            item_id=item.item_id,
            quantity=item.quantity
        )
        db.add(order_item)

    db.commit()

    return {"order_id": new_order.id, "total": total}
