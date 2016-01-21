import psycopg2

# Connect to an existing database
conn = psycopg2.connect("dbname=getting_started user=postgres password=Gatsby")

with conn:
    # Open a cursor to perform database operations
    cur = conn.cursor()

    cur.execute("SELECT name, state, year, warm_month, cold_month \
        FROM cities \
        INNER JOIN weather \
        ON name = city")

    join_out = cur.fetchall()
    
    print(join_out)
    print("join_out is type : {}  *** join_out[0] is type {}".format(type(join_out), type(join_out[0])))

"""Write a SQL statement which finds the mean of the average high temperatures for all of the cities within a state."""

with conn:
        cur = conn.cursor()
        cur.execute("SELECT name, state, avg(average_high) FROM weather group by(name, state)")
        print("avg by city state")
        print(cur.fetchall)

# persist the changes
# conn.commit()

# close the database connections  # do I need these if I'm using with - I don't think so.
# cur.close()
# conn.close()

# SELECT name, state, year, warm_month, cold_month 
# FROM cities 
# INNER JOIN weather 
#     ON name = city;