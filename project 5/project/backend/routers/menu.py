from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.menu_item import MenuItem
from schemas.menu_item import MenuItemCreate, MenuItem

router = APIRouter(prefix="/menu", tags=["Menu"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_menu(db: Session = Depends(get_db)):
    return db.query(MenuItem).all()

@router.post("/")
def create_menu_item(item: MenuItemCreate, db: Session = Depends(get_db)):
    new_item = MenuItem(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item
