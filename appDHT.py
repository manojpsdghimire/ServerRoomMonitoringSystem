#inserting data into the datatable
#using the sensors 

import sqlite3 as lite
import time
import Adafruit_DHT

#assigning database name
database = 'sensorData.db'

#getting data from the sensors
def get_data():
    DHT11Sensor = Adafruit_DHT.DHT11
    DHTpin = 27
    hum,temp = Adafruit_DHT.read_retry(DHT11Sensor, DHTpin)
    print(hum)
    print(temp)
    print("\Data from the table are:")
    print("INSERT")
    if hum is not None and temp is not None:
        hum = round(hum)
        temp = round(temp,1)
        logData(temp,hum,1,140,250)

#logging the data to the database
def logData (temp, hum, ping, download, upload):
    conn = lite.connect(database)
    curs=conn.cursor()
    curs.execute("INSERT INTO DHT_DATA VALUES(datetime('now'), (?),(?),(?),(?),(?))", (temp, hum, ping, download, upload))
    conn.commit()
    conn.close()
    
#printing data 
def printdata():
    conn = lite.connect(database)
    curs=conn.cursor()
    print("\Data from the table are:")
    for row in curs.execute("select* from DHT_data"):
        print(row)
    conn.close()
    
#main function
def main():
    
    for i in range(0,3):
        get_data()
        print("\Data from the table are:")
        printdata()
        time.sleep(0.5)
    
    
#execute the main function
main()
        



    

