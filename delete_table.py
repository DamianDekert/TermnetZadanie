import psycopg2
import os

# Get the DATABASE_URI from the environment variables
database_uri = os.getenv("DATABASE_URL", None)

# Connect to the database
conn = psycopg2.connect(database_uri)

# Create a cursor
cur = conn.cursor()

# Execute the SQL command to delete the table
cur.execute("DROP TABLE sessions")


# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
