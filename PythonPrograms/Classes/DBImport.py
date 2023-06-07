import sqlite3
import csv
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom


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

    def export_data_to_xml(self):
        try:
            self.cursor.execute("SELECT * FROM finedust;")
            finedust_data = self.cursor.fetchall()
            root_a = ET.Element("data")
            for row in finedust_data:
                item = ET.SubElement(root_a, 'item')
                sensor_id = ET.SubElement(item, 'sensor_id')
                sensor_id.text = str(row[1])
                sensor_type = ET.SubElement(item, 'sensor_type')
                sensor_type.text = str(row[2])
                location = ET.SubElement(item, 'location')
                location.text = str(row[3])
                lat = ET.SubElement(item, 'lat')
                lat.text = str(row[4])
                lon = ET.SubElement(item, 'lon')
                lon.text = str(row[5])
                timestamp = ET.SubElement(item, 'timestamp')
                timestamp.text = str(row[6])
                P1 = ET.SubElement(item, 'P1')
                P1.text = str(row[7])
                durP1 = ET.SubElement(item, 'durP1')
                durP1.text = str(row[8])
                ratioP1 = ET.SubElement(item, 'ratioP1')
                ratioP1.text = str(row[9])
                P2 = ET.SubElement(item, 'P2')
                P2.text = str(row[10])
                durP2 = ET.SubElement(item, 'durP2')
                durP2.text = str(row[11])
                ratioP2 = ET.SubElement(item, 'ratioP2')
                ratioP2.text = str(row[12])

            # ElementTree in eine Zeichenkette umwandeln
            xml_string_a = ET.tostring(root_a, encoding='utf-8').decode()

            # DTD-Deklaration zur XML-Datei hinzufügen
            xml_with_dtd_a = f'<?xml version="1.0" ?>\n<!DOCTYPE data SYSTEM "data.dtd">\n{xml_string_a}'

            # Schön formatierte XML-Datei speichern
            dom_a = minidom.parseString(xml_with_dtd_a)
            with open(str(self.path / "XMLFiles" / "exportedData-finedust.xml"), 'w', encoding='utf-8') as file_a:
                file_a.write(dom_a.toprettyxml(indent='    '))

            self.cursor.execute("SELECT * FROM tempandhumid;")
            tempandhumid_data = self.cursor.fetchall()
            root_b = ET.Element("data")
            for row in tempandhumid_data:
                item = ET.SubElement(root_b, 'item')
                sensor_id = ET.SubElement(item, 'sensor_id')
                sensor_id.text = str(row[1])
                sensor_type = ET.SubElement(item, 'sensor_type')
                sensor_type.text = str(row[2])
                location = ET.SubElement(item, 'location')
                location.text = str(row[3])
                lat = ET.SubElement(item, 'lat')
                lat.text = str(row[4])
                lon = ET.SubElement(item, 'lon')
                lon.text = str(row[5])
                timestamp = ET.SubElement(item, 'timestamp')
                timestamp.text = str(row[6])
                temperature = ET.SubElement(item, 'temperature')
                temperature.text = str(row[7])
                humidity = ET.SubElement(item, 'humidity')
                humidity.text = str(row[8])

            # ElementTree in eine Zeichenkette umwandeln
            xml_string_b = ET.tostring(root_b, encoding='utf-8').decode()

            # DTD-Deklaration zur XML-Datei hinzufügen
            xml_with_dtd_b = f'<?xml version="1.0" ?>\n<!DOCTYPE data SYSTEM "data.dtd">\n{xml_string_b}'

            # Schön formatierte XML-Datei speichern
            dom_b = minidom.parseString(xml_with_dtd_b)
            with open(str(self.path / "XMLFiles" / "exportedData-tempandhumid.xml"), 'w', encoding='utf-8') as file_b:
                file_b.write(dom_b.toprettyxml(indent='    '))

            print("Export der XML-Daten abgeschlossen.")
        except Exception as exception:
            print(str(exception))

    def main(self):
        self.connect_db()
        self.create_tables()
        self.import_csv()
        self.export_data_to_xml()
        self.connection.close()