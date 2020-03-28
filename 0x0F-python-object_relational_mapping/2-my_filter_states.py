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
    cursor.execute("SELECT id, name FROM states WHERE name='{}'\
    ORDER BY id ASC;".format(argument))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    database.close()
