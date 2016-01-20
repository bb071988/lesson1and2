import psycopg2
import pandas as pd

# Connect to an existing database
conn = psycopg2.connect("dbname=getting_started user=postgres password=Gatsby")


with conn:
    # Open a cursor to perform database operations
    cur = conn.cursor()
    cur.execute("SELECT * FROM weather")

    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns = cols)

print df.values
print df.describe
print df.describe(average_high)

# # persist the changes
# conn.commit()

# # close the database connections
# cur.close()
# conn.close()

