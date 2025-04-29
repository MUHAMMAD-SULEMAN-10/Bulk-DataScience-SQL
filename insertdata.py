# Step 2: Connect to the newly created DB
import mysql.connector
import pandas as pd

# Load data from CSV
df = pd.read_csv("e:/bulk of data/people_data.csv")

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='bulk_data'
)

cursor = mydb.cursor()

# Prepare insert query
insert_query = """
    INSERT INTO people_data1 (id, f_name, l_name, email, phone)
    VALUES (%s, %s, %s, %s, %s)
"""

# Convert DataFrame to list of tuples
data_to_insert = [tuple(row) for row in df.values]

# Execute all at once
cursor.executemany(insert_query, data_to_insert)
mydb.commit()

print(f"{cursor.rowcount} records inserted successfully into 'people_data1' table.")

cursor.close()
mydb.close()