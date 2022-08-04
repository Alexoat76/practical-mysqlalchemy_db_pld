#!/usr/bin/python3
# File: model_customer.py
# Author: BLUE TEAM (Alejandro Pineda, Andres Medina, Angelica Rodriguez,
#+                   Carlos Pardo, Alex Arevalo)

"""
Definition of a Customer and an instance Base
Inherits from SQLAlchemy Base and links to the MySQL table customers.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class customers(Base):
    """Represents a customer for a MySQL database."""

    __tablename__ = "customers"
    customerNumber = Column(Integer, primary_key=True)
    contactLastName = Column(String(128), nullable=False)
    addressLine1 = Column(String(128), nullable=False)
