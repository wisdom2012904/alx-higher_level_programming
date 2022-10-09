#!/usr/bin/python3
'''Scripts which add State Object and print the new states.id after creation
'''
import sys
from model_state import Base, State
from sqlachemy import (create_engine)
from sqlachemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_added_state = State(name='Louisiana')
    session.add(new_added_state)
    new_instance = session.query(State).filter_by(name='Louisiana'.first()
    print(new_instance.id)
    session.commit()
