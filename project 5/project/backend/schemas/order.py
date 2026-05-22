from pydantic import BaseModel
from typing import List

class OrderItemData(BaseModel):
    item_id: int
    quantity: int

class OrderCreate(BaseModel):
    items: List[OrderItemData]

class Order(BaseModel):
    id: int
    total_price: float

    class Config:
        orm_mode = True
