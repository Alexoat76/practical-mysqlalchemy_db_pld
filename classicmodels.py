#!/usr/bin/python3
# File:  classicmodels.py
# Author: BLUE TEAM (Alejandro Pineda, Andres Medina, Angelica Rodriguez,
#+                   Carlos Pardo, Alex Arevalo)

"""
This script return all customers from database via python
parameters given: username, password, database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_customer import customers

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for customers in session.query(customers).order_by(customers.customerNumber):
        print("{}: {}\t:\t {}".format(customers.customerNumber,
                                 customers.contactLastName, customers.addressLine1))

    session.close()
