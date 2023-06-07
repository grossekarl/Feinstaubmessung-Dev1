import Classes.Validator
from Classes.CSVDownloader import CSVDownloader
from Classes.DBImport import DBImport
from Classes.SQLQueries import SQLQueries
from pathlib import Path


class Main:
    def __init__(self):
        self.path = Path(__file__).parent.resolve()
        self.validator = Classes.Validator

    def download_data(self):
        print("Von wann sollen die CSV-Daten geholt werden?")
        print("Start-Datum(YYYY-MM-DD): ")
        start = input()
        print("End-Datum(YYYY-MM-DD): ")
        end = input()
        self.validator.validate_date(start)
        self.validator.validate_date(end)
        self.validator.validate_start_and_end_date(start, end)
        downloader = CSVDownloader(self.path, start, end)
        downloader.main()

    def import_data(self):
        importer = DBImport(self.path)
        importer.main(False)

    def export_data(self):
        importer = DBImport(self.path)
        importer.main(True)

    def query_db(self):
        print("Welche Abfrage wollen Sie ausführen?\n 1. Maximale, Minimale und Durchschittliche Temperatur eines Tages\n 2. Maximale, Minimale und Durchschittliche Luftfeuchtigkeit eines Tages\n 3. Maximale, Minimale und Durchschittliche Feinstaub eines Tages \n 4. Alle\n 1/2/3/4")
        sqlquery = input()
        self.validator.validate_sql_input(sqlquery)
        print("Von wann sollen die Werte ausgegeben werden?")
        print("Datum(YYYY-MM-DD): ")
        date = input()
        self.validator.validate_date(date)
        query_executor = SQLQueries(self.path, date)
        query_executor.main(sqlquery)

    def quit(self):
        raise SystemExit("Programm wurde abgebrochen")

    def end_of_program(self):
        raise SystemExit("Programm wurde beendet")

    def run(self):
        introduction = "Willkommen zur Feinstaubmessung! \n" \
                       "Dieses Programm kann sich die Daten eines Feinstaub-Sensors und eines Temperatur-und-Luftfeuchtigkeits-Sensor von dem Archiv: https://archive.sensor.community/ holen, \n" \
                       "diese in eine Datenbank importieren und SQL-Anfragen an der Datenbank ausführen. \n" \
                       "Das Programm wird fragen, ob Sie die Funktionalität ausführen wollen oder nicht. \n" \
                       "Sie können das Programm auch abbrechen, indem sie bei einer Frage anstatt 'y' oder 'n', 'stop' angeben. \n" \
                       "Die Sensor-Daten werden in lokale CSV-Dateien geschrieben. \n" \
                       "Bei jedem Datenbank Import werden die Daten des letzten Imports verloren. \n" \
                       "Wenn Sie erneut eine SQL-Anfrage an die Datenbank machen wollen, müssen sie Daten nicht erneut holen und importieren. \n"
        print(introduction)
        print("Sollen CSV-Daten der Sensoren geholt werden? y/n/stop")
        input1 = input()
        self.validator.validate_input(input1)
        if input1 == 'stop':
            self.quit()
        elif input1 == 'y':
            self.download_data()
            print("\nSollen die lokalen CSV-Daten in die Datenbank importiert werden? y/n/stop")
            input2 = input()
            self.validator.validate_input(input2)
            if input2 == 'stop':
                self.quit()
            elif input2 == 'y':
                self.import_data()
                print("\nWollen Sie die Datenbank Daten in XML-Dateien exportieren? y/n/stop")
                inputexport = input()
                self.validator.validate_input(inputexport)
                if inputexport == 'stop':
                    self.quit()
                if inputexport == 'y':
                    self.export_data()
                    print("\nWollen Sie eine SQL-Abfrage ausführen? y/n/stop")
                    input3 = input()
                    self.validator.validate_input(input3)
                    if input3 == 'stop':
                        self.quit()
                    if input3 == 'y':
                        self.query_db()
                        self.end_of_program()
                    if input3 == 'n':
                        self.end_of_program()
                if inputexport == 'n':
                    print("\nWollen Sie eine SQL-Abfrage ausführen? y/n/stop")
                    input3 = input()
                    self.validator.validate_input(input3)
                    if input3 == 'stop':
                        self.quit()
                    if input3 == 'y':
                        self.query_db()
                        self.end_of_program()
                    if input3 == 'n':
                        self.end_of_program()
            elif input2 == 'n':
                print("\nWollen Sie die Datenbank Daten in XML-Dateien exportieren? y/n/stop")
                inputexport = input()
                self.validator.validate_input(inputexport)
                if inputexport == 'stop':
                    self.quit()
                if inputexport == 'y':
                    self.export_data()
                    print("\nWollen Sie eine SQL-Abfrage ausführen? y/n/stop")
                    input3 = input()
                    self.validator.validate_input(input3)
                    if input3 == 'stop':
                        self.quit()
                    if input3 == 'y':
                        self.query_db()
                        self.end_of_program()
                    if input3 == 'n':
                        self.end_of_program()
                if inputexport == 'n':
                    print("\nWollen Sie eine SQL-Abfrage ausführen? y/n/stop")
                    input3 = input()
                    self.validator.validate_input(input3)
                    if input3 == 'stop':
                        self.quit()
                    if input3 == 'y':
                        self.query_db()
                        self.end_of_program()
                    if input3 == 'n':
                        self.end_of_program()
        elif input1 == 'n':
            print("\nSollen die lokalen CSV-Daten in die Datenbank importiert werden? y/n/stop")
            input2 = input()
            self.validator.validate_input(input2)
            if input2 == 'stop':
                self.quit()
            elif input2 == 'y':
                self.import_data()
                print("\nWollen Sie die Datenbank Daten in XML-Dateien exportieren? y/n/stop")
                inputexport = input()
                self.validator.validate_input(inputexport)
                if inputexport == 'stop':
                    self.quit()
                if inputexport == 'y':
                    self.export_data()
                    print("\nWollen Sie eine SQL-Abfrage ausführen? y/n/stop")
                    input3 = input()
                    self.validator.validate_input(input3)
                    if input3 == 'stop':
                        self.quit()
                    if input3 == 'y':
                        self.query_db()
                        self.end_of_program()
                    if input3 == 'n':
                        self.end_of_program()
                if inputexport == 'n':
                    print("\nWollen Sie eine SQL-Abfrage ausführen? y/n/stop")
                    input3 = input()
                    self.validator.validate_input(input3)
                    if input3 == 'stop':
                        self.quit()
                    if input3 == 'y':
                        self.query_db()
                        self.end_of_program()
                    if input3 == 'n':
                        self.end_of_program()
            elif input2 == 'n':
                print("\nWollen Sie die Datenbank Daten in XML-Dateien exportieren? y/n/stop")
                inputexport = input()
                self.validator.validate_input(inputexport)
                if inputexport == 'stop':
                    self.quit()
                if inputexport == 'y':
                    self.export_data()
                    print("\nWollen Sie eine SQL-Abfrage ausführen? y/n/stop")
                    input3 = input()
                    self.validator.validate_input(input3)
                    if input3 == 'stop':
                        self.quit()
                    if input3 == 'y':
                        self.query_db()
                        self.end_of_program()
                    if input3 == 'n':
                        self.end_of_program()
                if inputexport == 'n':
                    print("\nWollen Sie eine SQL-Abfrage ausführen? y/n/stop")
                    input3 = input()
                    self.validator.validate_input(input3)
                    if input3 == 'stop':
                        self.quit()
                    if input3 == 'y':
                        self.query_db()
                        self.end_of_program()
                    if input3 == 'n':
                        self.end_of_program()



