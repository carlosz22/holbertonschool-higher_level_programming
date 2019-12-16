#!/usr/bin/python3
""" Updates a State object to a database
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
    state_update = session.query(State).filter(State.id == 2).first()
    state_update.name = 'New Mexico'
    session.commit()
