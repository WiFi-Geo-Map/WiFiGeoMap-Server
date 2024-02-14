import sqlite3
#import ret from matrix
#import numpy as np
from shortest_path import shortest_path
from shortest_path import is_valid
from flask import Flask, request, jsonify

app = Flask(__name__)

def region(bs1,bs2,bs3,av):
    conn2 = sqlite3.connect('data.db')
    region=[]
    cursor = conn2.cursor()
    cursor.execute(f"select region from regions where (bssid = '{bs1}' or bssid ='{bs2}' or bssid = '{bs3}') and avg_val='{av}'")
    region.append(cursor.fetchone()[0])
    region.append(cursor.fetchone()[0])
    region.append(cursor.fetchone()[0])
    conn2.close()
    # print(region)
    res = max(set(region), key = region.count)
    # print("Element with highest frequency:\n",res)
    return res

# def nav(start,end):
#     adj_mat=ret
def route(start,end):
    sp=(ord(start[0])-65,int(start[1])-1)
    ep=(ord(end[0])-65,int(end[1])-1)
    # i=ord(start[0])-65
    # j=int(start[1])-1
    # p=ord(end[0])-65
    # q=int(end[1])-1
    # matrix = [
    # [0, 0, 0, 0],
    # [1, 1, 1, 1],
    # [0, 1, 1, 0],
    # [0, 1, 1, 0]]
    path=shortest_path(sp,ep)
    return path

    


# Define the process_input route
@app.route('/process_input', methods=['POST'])
def process_input():
    input_data = request.json  # Assuming JSON input
    # intensity, bssid = input_data['intensity'], input_data['bssid']
    bs1,bs2,bs3 = input_data['bs1'],input_data['bs2'],input_data['bs3']
    val1,val2,val3 = input_data['inten1'],input_data['inten2'],input_data['inten3']
    end_reg=input_data['dest']
    avg=int((val1+val2+val3)/3)
    print("Avg val", avg)
    print(type(bs1))

    # Connect to the existing SQL database
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Query the database to find the corresponding grid based on intensity and BSSID
    start_reg=region(bs1,bs2,bs3,avg)
    spath=route(start_reg,end_reg)
    rpath=[]

    # Convert indices to Region ids
    for i in spath:
        rpath.append(chr(i[0]+65)+str(i[1]+1))
    print(spath)
    print(rpath)

    # cursor.execute(f"SELECT classroom FROM class_bssid WHERE bssid='{bssid}'")
    # room=cursor.fetchone()
    # cursor.execute("SELECT grid_id, Classroom FROM intensity_bssid WHERE intensity=? AND bssid=?", (intensity, bssid))
    # result = cursor.fetchone()

    if True:
        #grid_id, classroom = result[0], result[1]

        # Query the database to retrieve the classroom details based on the grid_id
        #cursor.execute("SELECT room, floor, block, location FROM classrooms WHERE id=?", (grid_id,))
        #classroom_info = cursor.fetchone()

        # Close the database connection
        conn.close()
        # response_data ={'classroom':room[0],'bssid':bssid}
        #response_data = {'grid_name': grid_id, 'classroom': room, 'floor': classroom_info[1], 'block': classroom_info[2]}
        # print(response_data)
        #region('lol')
        return jsonify({
            "shortest path":rpath
        })
    else:
        return jsonify({'error': 'No matching records found for the given intensity and BSSID'})

if __name__ == '__main__':
    app.run()
