#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("""
        SELECT cities.id, cities.name, states.name FROM cities
        LEFT JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC;""")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
