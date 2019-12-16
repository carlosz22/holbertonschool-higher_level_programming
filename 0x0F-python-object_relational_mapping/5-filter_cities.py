#!/usr/bin/python3
""" Connect to the database and show states and cities
    filtered by user input
    includes protection from SQL Injection """

if __name__ == "__main__":
    import sys
    import MySQLdb

    if (len(sys.argv) >= 5):
        db = MySQLdb.connect(host='localhost',
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
        cursor = db.cursor()
        sql = "SELECT cities.name FROM cities \
               INNER JOIN states \
               ON cities.state_id = states.id \
               WHERE BINARY states.name=%(input)s \
               ORDER BY states.id ASC;"
        cursor.execute(sql, {'input': sys.argv[4]})
        rows = cursor.fetchall()
        cities_list = []
        for row in rows:
            cities_list.append(row[0])
        print(', '.join(cities_list))
        cursor.close()
        db.close()
