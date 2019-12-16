#!/usr/bin/python3
""" Connect to the database and show cities and states """

if __name__ == "__main__":
    import sys
    import MySQLdb
    print(len(sys.argv))

    if (len(sys.argv) >= 3):
        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
        cursor = db.cursor()
        sql = "SELECT cities.id, cities.name, \
               states.name FROM cities \
               INNER JOIN states \
               ON cities.state_id = states.id \
               ORDER BY cities.id ASC;"
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        db.close()
