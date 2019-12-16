#!/usr/bin/python3
""" Lists all State objects containing an 'a' from database
using SQLAlchemy """

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for id, name in session.query(State.id, State.name)\
            .filter(State.name.ilike('%a%')).order_by(State.id).all():

        print("{}: {}".format(id, name))
