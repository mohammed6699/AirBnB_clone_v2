#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy.Column import Column, string
from sqlalchemy.ext.declarative import declarative_base
from squalchemy.orm import relationship

#class User(BaseModel):
#    """This class defines a user by various attributes"""
#    email = ''
#    password = ''
#    first_name = ''
#    last_name = ''

class user(Base):
    __tablename__ = 'user'
    email = Column(string(128), nullable = False)
    password = Column(string(128), nullable = False)
    first_name = Column(string(128), nullable = True)
    last_name = Column(string(128), nullable = True)

    places = relationship('place', backref = 'user', cascade = 'all, delete-orphan')
    Review = relationship('Review', backref = user', cascade = 'all, delete-orphan')
