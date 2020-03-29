#!/usr/bin/python3
""" List all states """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_id = 2
    new_name = "New Mexico"
    states = session.query(State).filter(State.id == state_id)
    for state in states:
        state.name = new_name
    session.commit()
