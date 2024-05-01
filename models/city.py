#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from squalchamy.orm import relaionship, backref
from squalchemy import Column, String, ForeignKey
from models.state import State


#class City(BaseModel):
#    """ The city class, contains state ID and name """
#    state_id = ""
#    name = ""

class City(Base):
    """Define the class city"""
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship('Place', cascade="all, delete", backref='cities')
