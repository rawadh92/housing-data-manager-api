from sqlalchemy import Column, Integer, Float, String
from database import Base

class House(Base):
    __tablename__ = 'houses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    housing_median_age = Column(Integer, nullable=False)
    total_rooms = Column(Integer, nullable=False)
    total_bedrooms = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    households = Column(Integer, nullable=False)
    median_income = Column(Float, nullable=False)
    median_house_value = Column(Float, nullable=False)
    ocean_proximity = Column(String, nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "housing_median_age": self.housing_median_age,
            "total_rooms": self.total_rooms,
            "total_bedrooms": self.total_bedrooms,
            "population": self.population,
            "households": self.households,
            "median_income": self.median_income,
            "median_house_value": self.median_house_value,
            "ocean_proximity": self.ocean_proximity
        }
