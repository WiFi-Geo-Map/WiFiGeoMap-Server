import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the process_input route
@app.route('/process_input', methods=['POST'])
def process_input():
    input_data = request.json  # Assuming JSON input
    intensity, bssid = input_data['intensity'], input_data['bssid']

    print("Input from user", intensity, bssid)

    # Connect to the existing SQL database
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Query the database to find the corresponding grid based on intensity and BSSID
    cursor.execute("SELECT grid_id, Classroom FROM intensity_bssid WHERE intensity=? AND bssid=?", (intensity, bssid))
    result = cursor.fetchone()

    if result:
        grid_id, classroom = result[0], result[1]

        # Query the database to retrieve the classroom details based on the grid_id
        cursor.execute("SELECT room, floor, block, location FROM classrooms WHERE id=?", (grid_id,))
        classroom_info = cursor.fetchone()

        # Close the database connection
        conn.close()

        response_data = {'grid_name': grid_id, 'classroom': classroom_info[0], 'floor': classroom_info[1], 'block': classroom_info[2]}
        print(response_data)
        return jsonify(response_data)
    else:
        return jsonify({'error': 'No matching records found for the given intensity and BSSID'})

if __name__ == '__main__':
    app.run()
