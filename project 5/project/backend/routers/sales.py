from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.order import Order
from datetime import date

router = APIRouter(prefix="/sales", tags=["Sales"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/today")
def today_sales(db: Session = Depends(get_db)):
    today = date.today()
    sales = db.query(Order).filter(Order.order_time >= today).all()
    total = sum(float(o.total_price) for o in sales)
    return {"total_sales": total, "orders": sales}
