#!/usr/bin/python3
"""script that lists all states similar to the arg entered of the db"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    ob = db.cursor()
    ob.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))
    rows = ob.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    ob.close()
    db.close()
