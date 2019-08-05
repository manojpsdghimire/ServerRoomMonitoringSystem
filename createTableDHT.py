#creating a datatable

import sqlite3 as lite
import sys 

con = lcon=lite.connect('sensorData.db')

with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS DHT_DATA")
    cur.execute("CREATE TABLE DHT_DATA(timestamp DATETIME, temp NUMERIC, hum NUMERIC, ping NUMERIC,download NUMERIC,upload NUMERIC)")
