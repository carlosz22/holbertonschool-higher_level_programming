#!/usr/bin/python3
""" City model using SQLAlchemy """
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """ Class City """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, unique=True,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    state = relationship("State", back_populates="cities")

State.cities = relationship("City", order_by=City.id,
                            back_populates="state")
