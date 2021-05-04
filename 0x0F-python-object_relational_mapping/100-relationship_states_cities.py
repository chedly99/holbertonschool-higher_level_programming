#!/usr/bin/python3
"""
creates the  with the San 
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from sys import argv
from relationship_city import City

if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    s = State(name="California")
    s.cities = [City(name="San Francisco")]
    session.add(s)
    session.commit()
    session.close()
