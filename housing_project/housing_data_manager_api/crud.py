from sqlalchemy.orm import Session
from app import models, schemas
from app.database import SessionLocal

def get_houses():
    session = SessionLocal()
    try:
        return session.query(models.House).all()
    finally:
        session.close()

def create_house(house: schemas.HouseCreate):
    session = SessionLocal()
    db_house = models.House(**house.dict())
    session.add(db_house)
    session.commit()
    session.refresh(db_house)
    session.close()
    return db_house