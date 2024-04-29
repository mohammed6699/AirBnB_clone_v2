#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.Column import Column, string, ForeignKey, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

#class Place(BaseModel):
#    """ A place to stay """
#    city_id = ""
#    user_id = ""
#    name = ""
#    description = ""
#    number_rooms = 0
#    number_bathrooms = 0
#    max_guest = 0
#    price_by_night = 0
#    latitude = 0.0
#    longitude = 0.0
#    amenity_ids = []

class place(Base):
    __tablename__ = 'place'

    city_id = Column(string(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(string(60), ForeignKey('users.id'), nullable=False)
    name = Column(string(128), nullable=False)
    description = Column(string(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default = 0)
    number_bathrooms = Column(Integer, nullable=False, default = 0)
    max_guest = Column(Integer, nullable=False, default = 0)
    price_by_night = Column(Integer, nullable=False, default = 0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
