#!/usr/bin/python3
""" Lists first State object from database
filted by a name
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
    first_state = session.query(State.id, State.name)\
        .filter(State.name == sys.argv[4]).order_by(State.id).first()
    if (first_state is None):
        print("Not found")
    else:
        print("{}".format(first_state.id))
