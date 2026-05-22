from sqlalchemy import Column, Integer, String, DECIMAL
from database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    price = Column(DECIMAL(10,2))
    category = Column(String(50))
    image_url = Column(String(255))
