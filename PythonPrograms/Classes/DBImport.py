import sqlite3
import csv


class DBImport:
    def __init__(self, path):
        self.path = path
        self.cursor = None
        self.connection = None

    def connect_db(self):
        try:
            self.connection = sqlite3.connect(self.path / "DB" / "particlesmeasurements.db")
            self.cursor = self.connection.cursor()
        except Exception as error:
            print(str(error))

    def create_tables(self):
        try:
            # Delete and recreate table for finedust
            self.cursor.execute("DROP TABLE IF EXISTS finedust;")
            self.connection.commit()
            finedust_query_file = open(self.path / "DB" / "createfinedust.sql", "r")
            finedust_query = finedust_query_file.read()
            self.cursor.execute(finedust_query)
            self.connection.commit()
            finedust_query_file.close()
        except Exception as error:
            print(str(error))
        try:
            # Delete and recreate table for temperature and humidity
            self.cursor.execute("DROP TABLE IF EXISTS tempandhumid;")
            self.connection.commit()
            tempandhumid_query_file = open(self.path / "DB" / "createtempandhumid.sql", "r")
            tempandhumid_query = tempandhumid_query_file.read()
            self.cursor.execute(tempandhumid_query)
            self.connection.commit()
            tempandhumid_query_file.close()
        except Exception as error:
            print(str(error))

    def import_csv(self):
        # import csv data of sds011 in db table finedust
        try:
            sds_csv = open(self.path / "CSVFiles" / "Daten-SDS.csv", "r")
            reader = csv.DictReader(sds_csv)
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
            dht_csv = open(self.path / "CSVFiles" / "Daten-DHT.csv", "r")
            reader = csv.DictReader(dht_csv)
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
        self.connect_db()
        self.create_tables()
        self.import_csv()
        self.connection.close()
