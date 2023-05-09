import datetime
import urllib.request
import urllib.error
import csv


class CSVDownloader:
    def __init__(self, path, start_date, end_date):
        self.sensor_url = "https://archive.sensor.community/"
        self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        self.path = path

    def main(self):
        urlLists = self.get_urls()
        reader_lists = self.read_csv(urlLists)
        self.write_csv(reader_lists)
        print("Die CSV-Daten befinden sich nun im Ordner: ", self.path / 'CSVFiles')

    def get_urls(self):
        add_a_day = datetime.timedelta(days=1)
        date = self.start_date
        sds_list = []
        dht_list = []
        while date <= self.end_date:
            if 2022 >= date.year >= 2015:
                sensor_SDS011 = self.sensor_url + date.strftime("%Y") + "/" + date.strftime(
                    "%Y-%m-%d") + '/' + date.strftime(
                    "%Y-%m-%d") + '_sds011_sensor_3659.csv'
                sensor_DHT22 = self.sensor_url + date.strftime("%Y") + "/" + date.strftime(
                    "%Y-%m-%d") + '/' + date.strftime(
                    "%Y-%m-%d") + '_dht22_sensor_3660.csv'
                sds_list.append(sensor_SDS011)
                dht_list.append(sensor_DHT22)
                date = (date + add_a_day)
            else:
                sensor_SDS011 = self.sensor_url + date.strftime("%Y-%m-%d") + '/' + date.strftime(
                    "%Y-%m-%d") + '_sds011_sensor_3659.csv'
                sensor_DHT22 = self.sensor_url + date.strftime("%Y-%m-%d") + '/' + date.strftime(
                    "%Y-%m-%d") + '_dht22_sensor_3660.csv'
                sds_list.append(sensor_SDS011)
                dht_list.append(sensor_DHT22)
                date = (date + add_a_day)
        return {"sds": sds_list, "dht": dht_list}

    def read_csv(self, urls):
        sds_readers = []
        dht_readers = []
        for sds_url in urls['sds']:
            try:
                url_response = urllib.request.urlopen(sds_url)
            except (urllib.error.HTTPError, urllib.error.URLError):
                print("Die Daten von ", sds_url, " konnten nicht gefunden werden")
            else:
                csv_rows = [lines.decode('utf-8') for lines in url_response.readlines()]
                reader = csv.DictReader(csv_rows, delimiter=";")
                sds_readers.append(reader)
        for dht_url in urls['dht']:
            try:
                url_response = urllib.request.urlopen(dht_url)
            except (urllib.error.HTTPError, urllib.error.URLError):
                print("Die Daten von ", dht_url, " konnten nicht gefunden werden")
            else:
                csv_rows = [lines.decode('utf-8') for lines in url_response.readlines()]
                reader = csv.DictReader(csv_rows, delimiter=";")
                dht_readers.append(reader)
        return {"sds": sds_readers, "dht": dht_readers}

    def write_csv(self, readers):
        sds_file = open(self.path / "CSVFiles" / "Daten-SDS.csv", "w")
        dht_file = open(self.path / "CSVFiles" / "Daten-DHT.csv", "w")
        sds_writer = csv.DictWriter(sds_file,
                                    fieldnames=["sensor_id", "sensor_type", "location", "lat", "lon", "timestamp", "P1",
                                                "durP1", "ratioP1", "P2", "durP2", "ratioP2"])
        sds_writer.writeheader()
        dht_writer = csv.DictWriter(dht_file,
                                    fieldnames=["sensor_id", "sensor_type", "location", "lat", "lon", "timestamp",
                                                "temperature", "humidity"])
        dht_writer.writeheader()
        for sds_reader in readers['sds']:
            sds_writer.writerows(sds_reader)
        for dht_reader in readers['dht']:
            dht_writer.writerows(dht_reader)
        sds_file.close()
        dht_file.close()
