import sqlite3
import csv
import sys


class DBImport:
    def __init__(self, path):
        self.path = path
        self.cursor = None
        self.connection = None

    def connectdb(self):
        try:
            self.connection = sqlite3.connect(self.path / "DB" / "particlesmeasurements.db")
            self.cursor = self.connection.cursor()
        except Exception as error:
            print(str(error))

    def createtables(self):
        try:
            # Delete and recreate table for finedust
            self.cursor.execute("DROP TABLE IF EXISTS finedust;")
            self.connection.commit()
            finedustQueryFile = open(self.path / "DB" / "createfinedust.sql", "r")
            finedustQuery = finedustQueryFile.read()
            self.cursor.execute(finedustQuery)
            self.connection.commit()
            finedustQueryFile.close()
        except Exception as error:
            print(str(error))
        try:
            # Delete and recreate table for temperature and humidity
            self.cursor.execute("DROP TABLE IF EXISTS tempandhumid;")
            self.connection.commit()
            tempandhumidQueryFile = open(self.path / "DB" / "createtempandhumid.sql", "r")
            tempandhumidQuery = tempandhumidQueryFile.read()
            self.cursor.execute(tempandhumidQuery)
            self.connection.commit()
            tempandhumidQueryFile.close()
        except Exception as error:
            print(str(error))

    def importcsv(self):
        # import csv data of sds011 in db table finedust
        try:
            sdscsv = open(self.path / "CSVFiles" / "Daten-SDS.csv", "r")
            reader = csv.DictReader(sdscsv)
            values = []
            for row in reader:
                values.append((row['sensor_id'],
                               row['sensor_type'],
                               row['location'],
                               row['lat'],
                               row['lon'],
                               row['timestamp'],
                               row['P1'] if row['P1'] != "" else 'NULL',
                               row['durP1'] if row['durP1'] != "" else 'NULL',
                               row['ratioP1'] if row['ratioP1'] != "" else 'NULL',
                               row['P2'] if row['P2'] != "" else 'NULL',
                               row['durP2'] if row['durP2'] != "" else 'NULL',
                               row['ratioP2'] if row['ratioP2'] != "" else 'NULL'))
            self.cursor.executemany("INSERT INTO finedust (sensor_id, sensor_type, location, lat, lon, timestamp, P1, durP1, ratioP1, P2, durP2, ratioP2) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", values)
            self.connection.commit()
        except Exception as error:
            print(str(error))
        # import csv data of dht22 in db table tempandhumid
        try:
            dhtcsv = open(self.path / "CSVFiles" / "Daten-DHT.csv", "r")
            reader = csv.DictReader(dhtcsv)
            values = []
            for row in reader:
                values.append((row['sensor_id'],
                               row['sensor_type'],
                               row['location'],
                               row['lat'],
                               row['lon'],
                               row['timestamp'],
                               row['temperature'] if row['temperature'] != "" else 'NULL',
                               row['humidity'] if row['humidity'] != "" else 'NULL'))
            self.cursor.executemany("INSERT INTO tempandhumid (sensor_id, sensor_type, location, lat, lon, timestamp, temperature, humidity) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", values)
            self.connection.commit()
        except Exception as error:
            print(str(error))

    def main(self):
        self.connectdb()
        self.createtables()
        self.importcsv()
        self.connection.close()
