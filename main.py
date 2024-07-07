import os
import signal
from typing import Union
from fastapi import Depends, FastAPI

import uvicorn

from domain.item import Item
from services.cashservice import CashService

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, dataService = Depends(CashService)):
    return dataService.myCash(item_id)

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)