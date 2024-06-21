#!/usr/bin/python3

"""
list_states.py

This module connects to a MySQL database and lists all states
from a specified database.
It takes three command-line arguments: MySQL username,
MySQL password, and the database name.

Usage:
    python list_states.py <mysql_username> <mysql_password> <database_name>

Arguments:
    <mysql_username>    MySQL username to connect to the database
    <mysql_password>    MySQL password to connect to the database
    <database_name>     Name of the database to connect to

The script connects to a MySQL server running on localhost at
port 3306 and retrieves
all states from the specified database, sorted in ascending order
by states.id.
"""
import MySQLdb
import sys

def list_states(username, password, dbname):
    """
    Connects to the specified MySQL database and lists all states
    in ascending order by id.

    Parameters:
        username (str): The MySQL username.
        password (str): The MySQL password.
        dbname (str): The name of the database.

    Returns:
        None

    Prints:
        Each state as a tuple (id, name).
    """
    try:
        db = MySQLdb.connect(host="localhost", user=username,
                passwd=password, db=dbname, port=3306)

        cursor = db.cursor()
        query = "SELECT * FROM states ORDER BY id ASC;"
        cursor.execute(query)
        results = cursor.fetchall()

        for row in results:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error {e}")

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    list_states(username, password, dbname)
