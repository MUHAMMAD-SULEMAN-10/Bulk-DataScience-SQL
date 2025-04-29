import mysql.connector

# Step 1: Connect without selecting a DB
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678'
)

cursor = mydb.cursor()
cursor.execute("CREATE DATABASE bulk_data")
print("Database 'bulk_data' created.")

cursor.close()
mydb.close()

# Step 2: Connect to the newly created DB
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='bulk_data'
)

if mydb.is_connected():
    print("Connection to 'bulk_data' is established.")
