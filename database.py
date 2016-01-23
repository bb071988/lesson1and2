import psycopg2
import pandas as pd

weather = (
    {'city': 'Las Vegas', 'year': 2013, 'warm_month': 'July', 'cold_month': 'December'},
    {'city': 'Atlanta', 'year': 2013, 'warm_month': 'July', 'cold_month': 'January'})

cities = ({'city':'Las Vegas','state':'NV'},
        {'city':'Atlanta','state':'GA'})

# Connect to an existing database
conn = psycopg2.connect("dbname=getting_started user=postgres password=Gatsby")

with conn:
    #open the cursor
    cur = conn.cursor()

    # set up the tables.
    cur.execute("DROP TABLE IF EXISTS weather2")
    cur.execute("DROP TABLE IF EXISTS cities2")

    cur.execute("CREATE TABLE weather2 (LIKE weather INCLUDING ALL)")
    cur.execute("CREATE TABLE cities2 (LIKE cities INCLUDING ALL)")

    conn.commit()

    
with conn:
    #open the cursor
    cur = conn.cursor()
    # load the data # use all %s here have to use field names too
    cur.executemany("INSERT INTO cities2 VALUES (%(city)s, %(state)s)", cities)
    cur.executemany("INSERT INTO weather2 VALUES(%(city)s, %(year)s, %(warm_month)s, %(cold_month)s)", weather) #city year warm_month cold_month average_high
    conn.commit()

with conn:
    #open the cursor
    cur = conn.cursor()
    # Join the data
    cur.execute("SELECT name, state, year, warm_month \
        FROM cities2 INNER JOIN weather2 \
        ON name = city WHERE warm_month = 'July'")

    rows = cur.fetchall()

    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns = cols)

    print(df.values)

    print("The cities that are warmest in July are:")
    for record in rows:
        print("{}, {}".format(record[0],record[1]))

