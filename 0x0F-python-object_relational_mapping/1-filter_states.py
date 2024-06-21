#!/usr/bin/python3

"""
0-select_states.py

This script connects to a MySQL database and lists all states
with a name starting with 'N' from a specified database.
It takes three command-line arguments: MySQL username,
MySQL password, and the database name.

Usage:
    python 0-select_states.py <mysql_username> <mysql_password> <database_name>
"""


if __name__ == "__main__":

    import MySQLdb
    import sys

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC;"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
