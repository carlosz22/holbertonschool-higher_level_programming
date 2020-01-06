#!/usr/bin/python3
""" State model using SQLAlchemy """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ Class State """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state")
