#!/usr/bin/python3
""" List all states """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    dataname = argv[3]
    argument = argv[4]
    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=username,
                               passwd=password,
                               db=dataname)
    cursor = database.cursor()
    query = "SELECT id, name FROM states WHERE name=%s\
    ORDER BY id ASC;"
    cursor.execute(query, (argument, ))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    database.close()
