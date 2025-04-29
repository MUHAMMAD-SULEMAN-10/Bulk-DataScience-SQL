import mysql.connector

# Step 1: Connect to the DB
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='bulk_data'
)

if mydb.is_connected():
    print("Connection to 'bulk_data' is established.")

cursor = mydb.cursor()

# Step 2: Execute SELECT query to retrieve all records
cursor.execute("SELECT * FROM people_data1")

# Step 3: Fetch all records
records = cursor.fetchall()

# Step 4: Display the records
for record in records:
    print(record)

cursor.close()
mydb.close()
