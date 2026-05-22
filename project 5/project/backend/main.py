from fastapi import FastAPI
from routers import menu, pos, sales
from database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(menu.router)
app.include_router(pos.router)
app.include_router(sales.router)
