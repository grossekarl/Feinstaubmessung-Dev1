import datetime
import urllib.request

class CSVDownloader:
    def __init__(self, saveFileToPath):
        self.sensorURL = "http://archive.sensor.community/"
        self.startDate = datetime.date(2022, 1, 1)
        self.endDate = datetime.date(2023, 2, 21)
        self.saveFileToPath = saveFileToPath
        self.list = []

    def main(self):
        self.makeListOfURLs()
        print(self.list)
            urllib.request.urlretrieve(x, )

   # def getSensorName():

    def makeListOfURLs(self):
        delta = datetime.timedelta(days=1)
        date = self.startDate
        while date <= self.endDate:
            sensorSDS011 = self.sensorURL + date.strftime("%Y-%m-%d") + '/' + date.strftime("%Y-%m-%d") + '_sds011_sensor_3659.csv'
            sensorDHT22 = self.sensorURL + date.strftime("%Y-%m-%d") + '/' + date.strftime("%Y-%m-%d") + '_dht22_sensor_3660.csv'
            self.list.append(sensorSDS011)
            self.list.append(sensorDHT22)
         #   urllib.request.urlretrieve(sensorSDS011, date.strftime("%Y-%m-%d") + '_sds011.csv')
            date += delta

downloader = CSVDownloader('__DIR__')
downloader.main()