#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from squalchamy.orm import relaionship
from squalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base


#class City(BaseModel):
#    """ The city class, contains state ID and name """
#    state_id = ""
#    name = ""

class City(Base):
    __tablename__ = 'Cities'

    state_id = Column(string(60), nullable = False)
    name = Column(string(128), nullable = False)

    places = relationship('place', backref = 'citis', cascade='all, delete-orphan')
