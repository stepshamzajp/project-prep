from sqlalchemy import Column, Integer, DECIMAL, DateTime
from database import Base
from datetime import datetime

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    order_time = Column(DateTime, default=datetime.now)
    total_price = Column(DECIMAL(10,2))
