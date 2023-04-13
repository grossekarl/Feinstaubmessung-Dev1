import datetime
import urllib.request
import urllib.error
import csv
import sys

class CSVDownloader:
    def __init__(self, path, startDate, endDate):
        self.sensorURL = "https://archive.sensor.community/"
        self.startDate = datetime.datetime.strptime(startDate, '%Y-%m-%d')
        self.endDate = datetime.datetime.strptime(endDate, '%Y-%m-%d')
        self.path = path

    def main(self):
        urlLists = self.geturls()
        readerLists = self.readcsv(urlLists)
        self.writecsv(readerLists)

    def geturls(self):
        delta = datetime.timedelta(days=1)
        date = self.startDate
        sdsList = []
        dhtList = []
        while date <= self.endDate:
            if 2022 >= date.year >= 2015:
                sensorSDS011 = self.sensorURL + date.strftime("%Y") + "/" + date.strftime(
                    "%Y-%m-%d") + '/' + date.strftime(
                    "%Y-%m-%d") + '_sds011_sensor_3659.csv'
                sensorDHT22 = self.sensorURL + date.strftime("%Y") + "/" + date.strftime(
                    "%Y-%m-%d") + '/' + date.strftime(
                    "%Y-%m-%d") + '_dht22_sensor_3660.csv'
                sdsList.append(sensorSDS011)
                dhtList.append(sensorDHT22)
                date = (date + delta)
            else:
                sensorSDS011 = self.sensorURL + date.strftime("%Y-%m-%d") + '/' + date.strftime(
                    "%Y-%m-%d") + '_sds011_sensor_3659.csv'
                sensorDHT22 = self.sensorURL + date.strftime("%Y-%m-%d") + '/' + date.strftime(
                    "%Y-%m-%d") + '_dht22_sensor_3660.csv'
                sdsList.append(sensorSDS011)
                dhtList.append(sensorDHT22)
                date = (date + delta)
        return {"sds": sdsList, "dht": dhtList}

    def readcsv(self, urls):
        sdsReaders = []
        dhtReaders = []
        for sdsUrl in urls['sds']:
            try:
                urlResponse = urllib.request.urlopen(sdsUrl)
            except (urllib.error.HTTPError, urllib.error.URLError):
                print(sdsUrl + " not found")
            else:
                csvRows = [l.decode('utf-8') for l in urlResponse.readlines()]
                reader = csv.DictReader(csvRows, delimiter=";")
                sdsReaders.append(reader)
        for dhtUrl in urls['dht']:
            try:
                urlResponse = urllib.request.urlopen(dhtUrl)
            except (urllib.error.HTTPError, urllib.error.URLError):
                print(dhtUrl + " not found")
            else:
                csvRows = [l.decode('utf-8') for l in urlResponse.readlines()]
                reader = csv.DictReader(csvRows, delimiter=";")
                dhtReaders.append(reader)
        return {"sds": sdsReaders, "dht": dhtReaders}

    def writecsv(self, readers):
        sdsFile = open(self.path / "CSVFiles" / "Daten-SDS.csv", "w")
        dhtFile = open(self.path / "CSVFiles" / "Daten-DHT.csv", "w")
        sdsWriter = csv.DictWriter(sdsFile,
                                   fieldnames=["sensor_id", "sensor_type", "location", "lat", "lon", "timestamp", "P1",
                                               "durP1", "ratioP1", "P2", "durP2", "ratioP2"])
        sdsWriter.writeheader()
        dhtWriter = csv.DictWriter(dhtFile,
                                   fieldnames=["sensor_id", "sensor_type", "location", "lat", "lon", "timestamp",
                                               "temperature", "humidity"])
        dhtWriter.writeheader()
        for sdsReader in readers['sds']:
            sdsWriter.writerows(sdsReader)
        for dhtReader in readers['dht']:
            dhtWriter.writerows(dhtReader)
        sdsFile.close()
        dhtFile.close()
