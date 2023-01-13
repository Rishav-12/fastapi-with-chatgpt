from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items = []

class Item(BaseModel):
    """defines a schema for an item"""
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.post("/items/")
async def create_item(item: Item):
    items.append(item)
    return {"item": item.dict()}

@app.get("/items/")
async def read_items():
    return {"items": [item.dict() for item in items]}
