#!/usr/bin/python3
"""Lists all states via SQLAlchemy"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@127.0.0.1:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    state = State(name="California")
    city = City(name='San Francisco')

    state.cities.append(city)

    session.add(state)
    session.commit()
    session.close()
