#!/usr/bin/python3
"""
that prints all City objects from the database
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))

    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()

    for statx, citx in session.query(State, City)\
                              .filter(State.id == City.state_id)\
                              .order_by(City.id).all():
        print("{}: ({}) {}".format(statx.name, citx.id, citx.name))
    session.close()
