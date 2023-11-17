import pandas as pd
import json 
import csv
fp=open('./bssid.json','r')
data=json.load(fp)
keyList = data.keys()
valueList = data.values()

rows = zip(keyList, valueList)

with open('test.csv', 'w') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
fp.close()
