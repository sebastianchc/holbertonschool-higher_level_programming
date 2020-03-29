#!/usr/bin/python3
""" List all states """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    state_cities = ""
    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=argv[1],
                               passwd=argv[2],
                               db=argv[3])
    cursor = database.cursor()
    query = "SELECT cities.name FROM cities JOIN states "
    query = query + "ON cities.state_id=states.id WHERE states.name=%s "
    query = query + "ORDER BY cities.id ASC;"
    cursor.execute(query, (argv[4], ))
    rows = cursor.fetchall()
    cities = [row[0] for row in rows]
    print(', '.join(cities))

    cursor.close()
    database.close()
