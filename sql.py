import sqlite3

# Connect to SQLite
try:
    connection = sqlite3.connect(r'C:\Users\Chintan\Desktop\healthcare_dataset\tsec.sqlite')
    print("Connected to database")
except Exception as e:
    print("Failed to connect to database:", e)
    exit(1)

# Create a cursor object
cursor = connection.cursor()

# Check if the table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students';")
if not cursor.fetchone():
    print("No such table: students")
else:
    # Insert more records (if needed)


    # Display all records
    try:
        print("The inserted records are:")
        data = cursor.execute("SELECT * FROM students")
        for row in data:
            print(row)
    except sqlite3.OperationalError as e:
        print("Error querying data:", e)

# Commit changes in the database
connection.commit()

# Close the database connection
connection.close()