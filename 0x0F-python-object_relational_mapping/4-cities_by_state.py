#!/usr/bin/python3
"""
Script the list and filter the name the states
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    pas = sys.argv[2]
    dbn = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=pas, db=dbn)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM states join cities
                on cities.state_id = states.id ORDER BY cities.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
