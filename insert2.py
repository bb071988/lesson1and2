import psycopg2

# Connect to an existing database
conn = psycopg2.connect("dbname=getting_started user=postgres password=Gatsby")

# cities = (('Las Vegas', 'NV'),
#                     ('Atlanta', 'GA'))

# weather = (('Las Vegas', 2013, 'July', 'December'),  # this gives tuple indicies must be integers not string.
#                      ('Atlanta', 2013, 'July', 'January'))

weather = (
    {'city': 'Las Vegas', 'year': 2013, 'warm_month': 'July', 'cold_month': 'December'},
    {'city': 'Atlanga', 'year': 2013, 'warm_month': 'July', 'cold_month': 'January'})

cities = ({'city':'Las Vegas','state':'NV'},
        {'city':'Atlanta','state':'GA'})

with conn:
    # Open a cursor to perform database operations
    cur = conn.cursor()
    cur.executemany("INSERT INTO cities VALUES (%(city)s, %(state)s)", cities)
    # cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(%(city)s, %(year)s, %(warm_month)s, %(cold_month)s)", weather) #city year warm_month cold_month average_high
    # use all %s here have to use field names too

    # cur.executemany("INSERT INTO weather VALUES(?,?,?,?)", weather)

    # "INSERT INTO myTable VALUES (%(num)d, %(text)s)", rows


# persist the changes
conn.commit()

# close the database connections
cur.close()
conn.close()

