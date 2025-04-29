import mysql.connector

# Step 2: Connect to the newly created DB
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='bulk_data'
)

if mydb.is_connected():
    print("Connection to 'bulk_data' is established.")

cursor = mydb.cursor()

# Create the table with a correct VARCHAR size for the 'phone' column
# cursor.execute("""
#     CREATE TABLE people_data1 (
#         id INT PRIMARY KEY,
#         f_name VARCHAR(50),
#         l_name VARCHAR(50),
#         email VARCHAR(100),
#         phone VARCHAR(15)  
#     )
# """)

# print("Table 'people_data1' has been created successfully.")

# If you need to modify the table again in the future, you can use ALTER TABLE
cursor.execute("""
    ALTER TABLE people_data1
    MODIFY phone VARCHAR(50);
""")

mydb.commit()
print("Changes committed successfully.")

cursor.close()
mydb.close()
