#!/usr/bin/python3
"""Displays all values in the states table where name matches the
argument safely from MySQL injection."""

if __name__ == "__main__":
    import MySQLdb
    import sys

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()

    # Create the SQL query using parameterized queries to prevent SQL injection
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC;"
    cur.execute(query, (sys.argv[4],))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
