#!/usr/bin/python3
"""script that lists all states of the db starting with N"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    ob = db.cursor()
    ob.execute("SELECT * FROM states ORDER BY id ASC")
    rows = ob.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    ob.close()
    db.close()
