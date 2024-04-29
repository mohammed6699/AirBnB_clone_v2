#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy.Column import Column, string, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

#class Review(BaseModel):
#    """ Review classto store review information """
#    place_id = ""
#    user_id = ""
#    text = ""

class Reviem(Base):
    __tablename__= 'reviews'

    text = Column(string(1024), nullable = False)
    place_id = Column(string(60),ForeignKey('places.id'),  nullable = False)
    user_id = Column(string(60), ForeignKey('users.id'), nullable = False)
