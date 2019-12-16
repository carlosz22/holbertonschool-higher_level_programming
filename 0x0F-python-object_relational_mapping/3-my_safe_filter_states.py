#!/usr/bin/python3
""" Connect to the database and show states
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
        sql = "SELECT * FROM states \
               WHERE name=%(input)s \
               ORDER BY id ASC;"
        cursor.execute(sql, {'input': sys.argv[4]})
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        db.close()
