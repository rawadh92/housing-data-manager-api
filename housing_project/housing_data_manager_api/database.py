import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import House
from schemas import HouseCreate


# Configuration de la base de données via les variables d'environnement
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/housing")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)