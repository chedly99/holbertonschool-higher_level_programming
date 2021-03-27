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
    statex = sys.argv[4]

    for i in statex:
        if i == ';' or i == '':
            sys.exit()
    print(statex)
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=pas, db=dbn)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name='{:s}' ORDER BY states.id"
                .format(statex))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
