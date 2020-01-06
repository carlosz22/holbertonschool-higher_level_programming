#!/usr/bin/python3
""" Deletes a State object to a database
using SQLAlchemy """

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state, city_id, city in session.query(State.name, City.id, City.name)\
            .join(City, State.cities).order_by(City.id).all():
        print("{}: ({}) {}".format(state, city_id, city))
