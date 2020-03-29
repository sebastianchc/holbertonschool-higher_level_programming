#!/usr/bin/python3
""" List all states """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=argv[1],
                               passwd=argv[2],
                               db=argv[3])
    cursor = database.cursor()
    query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC;"
    query = query.format(argv[4])
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    database.close()
