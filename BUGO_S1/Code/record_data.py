from datetime import datetime
import pymysql
import time

class record_data:
    def __init__(self, host, user, passwd, db, port):
        #For Server Connecting
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port
        self.Maria = pymysql.connect(host = self.host, user = self.user, passwd = self.passwd, db = self.db, port = self.port)
        self.Cursor = self.Maria.cursor()

    def record_data(self, sensor):
        temp = sensor.t
        humi = sensor.h
        wave = sensor.w

        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        print(f"{date}\nTEMP= {temp} HUMI= {humi} WAVE= {wave}")

        #data input at SQL

        Query = 'INSERT INTO SENSORS_INFO VALUES(%s, %s, %s, %s)'   #usertable == table 
        values = [(date, humi, temp, wave)]
        
        self.Cursor.executemany(Query, values)    
        self.Maria.commit()          #Input and save data at Server
        time.sleep(3)
if __name__ == '__main__':
    rec = record_data()
    rec.record_data()
