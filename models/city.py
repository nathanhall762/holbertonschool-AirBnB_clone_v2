#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel

#Update City: (models/city.py)

#City inherits from BaseModel and Base (respect the order)
#Add or replace in the class City:
    #class attribute __tablename__ -
        #represents the table name, cities
    #class attribute name
        #represents a column containing a string (128 characters)
        #can’t be null
    #class attribute state_id
        #represents a column containing a string (60 characters)
        #can’t be null
        #is a foreign key to states.id

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship(
        "Place",
        backref='cities',
        cascade="all, delete",
        passive_deletes=True)