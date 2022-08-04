#!/usr/bin/python3
# File:  found_customer.py
# Author: BLUE TEAM (Alejandro Pineda, Andres Medina, Angelica Rodriguez,
#+                   Carlos Pardo, Alex Arevalo)

"""
This script return state id given state name; SQL injection free
parameters given: username, password, database, customer last name to match
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_customer import Base, customers

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    found = False
    for customers in session.query(customers):
        if customers.contactLastName == sys.argv[4]:
            print("{}".format(customers.customerNumber))
            found = True
            break
    if found is False:
        print("Not found")
    session.close()
