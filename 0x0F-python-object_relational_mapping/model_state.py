#!/usr/bin/python3
"""Defines a State class and connects to a MySQL database using SQLAlchemy."""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

# Define the base class
Base = declarative_base()

# Define the State class
class State(Base):
    """State class that links to the MySQL table states."""
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./model_state.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Create the engine and connect to the MySQL database using sys.argv directly
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    
    # Create all tables in the database
    Base.metadata.create_all(engine)
