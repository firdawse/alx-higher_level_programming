#!/usr/bin/python3
"""script that lists all states similar to the arg entered of the db"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    ob = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    state_name = (argv[4],)
    ob.execute(query, state_name)
    rows = ob.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    ob.close()
    db.close()
