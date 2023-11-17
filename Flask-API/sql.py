import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('data.db')  # Replace 'your_database_name' with the desired name of your database file
cursor = conn.cursor()

# Create a table to store the intensity-bssid mapping
cursor.execute('''CREATE TABLE intensity_bssid (
                    id INTEGER PRIMARY KEY,
                    Classroom TEXT,
                    intensity INTEGER,
                    bssid TEXT,
                    grid_id INTEGER
                )''')

# Create a table to store the classroom information
cursor.execute('''CREATE TABLE classrooms (
                    id INTEGER PRIMARY KEY,
                    room TEXT,
                    floor INTEGER,
                    block TEXT,
                    location TEXT
                )''')

# Populate the intensity-bssid mapping table with sample data
cursor.execute("INSERT INTO intensity_bssid (Classroom, intensity, bssid, grid_id) VALUES (?, ?, ?, ?)", ('A407',65, 'bssid1', 1))
cursor.execute("INSERT INTO intensity_bssid (Classroom, intensity, bssid, grid_id) VALUES (?, ?, ?, ?)", ('A407',70, 'bssid2', 2))
# Add more sample data as needed

# Populate the classroom information table with sample data
cursor.execute("INSERT INTO classrooms (room, floor, block, location) VALUES (?, ?, ?, ?)", ('A407', 4, 'A', '(x4,y4)'))
cursor.execute("INSERT INTO classrooms (room, block, floor, location) VALUES (?, ?, ?, ?)", ('A207', 2, 'B', '(x2,y2)'))
# Add more sample data as needed

# Commit the changes and close the database connection
conn.commit()
conn.close()
