import sqlite3


class SQLQueries:
    def __init__(self, path, date):
        self.path = path
        self.cursor = None
        self.connection = None
        self.date = date

    def build_connection(self):
        try:
            self.connection = sqlite3.connect(self.path / "DB" / "particlesmeasurements.db")
            self.cursor = self.connection.cursor()
        except Exception as error:
            print(str(error))

    def close_connection(self):
        try:
            self.connection.commit()
            self.connection.close()
        except Exception as error:
            print(str(error))

    def tables_exist(self):
        try:
            result = []
            query = "SELECT name FROM sqlite_master WHERE type='table' AND name='tempandhumid';"
            self.cursor.execute(query)
            result.append(self.cursor.fetchone())
            query = "SELECT name FROM sqlite_master WHERE type='table' AND name='finedust';"
            self.cursor.execute(query)
            result.append(self.cursor.fetchone())
            if None in result:
                print('Es wurden noch keine Daten in die Datenbank importiert. Es können keine SQL-Abfragen ausgeführt werden.')
                raise SystemExit
        except Exception as error:
            print(str(error))

    def select_temperature(self):
        try:
            query = "SELECT MAX(temperature) AS max_temp, MIN(temperature) as min_temp, AVG(temperature) as avg_temp FROM tempandhumid WHERE timestamp LIKE ?;"
            self.cursor.execute(query, (self.date + '%', ))
            result = list(self.cursor.fetchone())
            if None in result:
                print('Die Abfrage hat keine Werte zurückgegeben.')
                return
            print("---------------------------------------------")
            print("Maximale Temperatur: ", round(result[0], 2))
            print("Minimale Temperatur: ", round(result[1], 2))
            print("Durchschnittliche Temperatur: ", round(result[2], 2))
            print("---------------------------------------------")
        except Exception as error:
            print(str(error))

    def select_humidity(self):
        try:
            query = "SELECT MAX(humidity) AS max_humid, MIN(humidity) as min_humid, AVG(humidity) as avg_humid FROM tempandhumid WHERE timestamp LIKE ?;"
            self.cursor.execute(query, (self.date + '%', ))
            result = list(self.cursor.fetchone())
            if None in result:
                print('Die Abfrage hat keine Werte zurückgegeben.')
                return
            print("---------------------------------------------")
            print("Maximale Luftfeuchtigkeit: ", round(result[0], 2))
            print("Minimale Luftfeuchtigkeit: ", round(result[1], 2))
            print("Durchschnittliche Luftfeuchtigkeit: ", round(result[2], 2))
            print("---------------------------------------------")
        except Exception as error:
            print(str(error))

    def select_finedust(self):
        try:
            query = "SELECT MAX(P1) AS max_p1, MIN(P1) as min_p1, AVG(P1) as avg_p1, MAX(P2) AS max_p2, MIN(P2) as min_p2, AVG(P2) as avg_p2 FROM finedust WHERE timestamp LIKE ?;"
            self.cursor.execute(query, (self.date + '%', ))
            result = list(self.cursor.fetchone())
            if None in result:
                print('Die Abfrage hat keine Werte zurückgegeben.')
                return
            print("---------------------------------------------")
            print("Maximale Feinstaub P1: ", round(result[0], 2))
            print("Minimale Feinstaub P1: ", round(result[1], 2))
            print("Durchschnittliche Feinstaub P1: ", round(result[2], 2))
            print("---------------------------------------------")
            print("Maximale Feinstaub P2: ", round(result[3], 2))
            print("Minimale Feinstaub P2: ", round(result[4], 2))
            print("Durchschnittliche Feinstaub P2: ", round(result[5], 2))
            print("---------------------------------------------")
        except Exception as error:
            print(str(error))

    def main(self, query):
        self.build_connection()
        self.tables_exist()
        if query == '1':
            self.select_temperature()
        if query == '2':
            self.select_humidity()
        if query == '3':
            self.select_finedust()
        if query == '4':
            self.select_temperature()
            self.select_humidity()
            self.select_finedust()
        self.close_connection()
