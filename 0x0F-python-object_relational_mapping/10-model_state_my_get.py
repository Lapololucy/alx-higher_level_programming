#!/usr/bin/python3
"""Lists all states via SQLAlchemy"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    state = session.query(State).filter(
                State.name.like("{}".format(
                          sys.argv[4].replace("'", "''")))).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()
