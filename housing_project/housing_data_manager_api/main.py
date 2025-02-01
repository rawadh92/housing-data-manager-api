from fastapi import FastAPI, HTTPException
from app import models, schemas, database, crud
from models import House
from schemas import HouseCreate


app = FastAPI()

@app.get("/houses", response_model=list[schemas.House])
async def get_houses():
    return crud.get_houses()

@app.post("/houses", response_model=schemas.House)
async def create_house(house: schemas.HouseCreate):
    return crud.create_house(house) 