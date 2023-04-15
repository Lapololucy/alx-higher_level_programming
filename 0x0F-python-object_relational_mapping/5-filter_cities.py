#!/usr/bin/python3
"""This script lists all ``states`` from a given database."""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    cur = db.cursor()
    cur.execute("""SELECT  C.name
                   FROM cities C INNER JOIN states S ON S.id = C.state_id
                   WHERE S.name = '{}'
                   ORDER BY C.id ASC""".format(sys.argv[4].replace("'", "''")))
    rows = cur.fetchall()
    for i, row in enumerate(rows):
        print(row[0], end='')
        if i < len(rows) - 1:
            print(', ', end='')
    print()
    cur.close()
    db.close()
