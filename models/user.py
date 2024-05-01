#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """User class"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship('Place', cascade='all, delete-orphan',
                          backref='user')
    reviews = relationship('Review', cascade='all, delete-orphan',
                           backref='user')
