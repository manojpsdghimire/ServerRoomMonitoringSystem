#inserting data into the datatable

import sqlite3 as lite
import sys 

conn = lite.connect('sensorData.db')
curs=conn.cursor()

#function to insert data into the table
def insert_data(temp, hum, ping, download, upload):
    curs.execute("INSERT INTO DHT_DATA VALUES(datetime('now'), (?),(?),(?),(?),(?))", (temp, hum, ping, download, upload))
    conn.commit()
    
#call the function to add the data to the table
insert_data(20.5,30.0,2,145,257); 
insert_data(20.5,38.0,2,147,267);
insert_data(20.5,35.0,2,150,297);

#print the database content
print("\Data from the table are:")
for row in curs.execute("select* from DHT_data"):
    print(row)

#closing the database
conn.close()


    


