#creating a datatable

import sqlite3 as lite
import sys 

con = lite.connect('sensorData.db')

with con: 
    cur = con.cursor() 
    cur.execute("INSERT INTO DHT_DATA VALUES (datetime('now'), 20.5,31.5,2,145,85)")
    cur.execute("INSERT INTO DHT_DATA VALUES(datetime('now'), 20.0,32,2,345,285)")
    cur.execute("INSERT INTO DHT_DATA VALUES(datetime('now'), 20.5,30,2,545,785)")
    

