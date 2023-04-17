from Classes.CSVDownloader import CSVDownloader
from Classes.DBImport import DBImport
from Classes.SQLQueries import SQLQueries
from pathlib import Path
import sys

def downloaddata(start, end):
    if start != "" and end != "":
        downloader = CSVDownloader(Path(__file__).parent.resolve(), start, end)
        downloader.main()
        print("Die CSV-Daten befinden sich nun im Ordner: ", Path(__file__).parent.resolve() / 'CSVFiles')
    else:
        print("Es wurden kein Start- und/oder End-Datum angegeben")
        sys.exit()
def importdata():
    importer = DBImport(Path(__file__).parent.resolve())
    importer.main()
def querydb(date, query):
    queryexecutor = SQLQueries(Path(__file__).parent.resolve(), date)
    queryexecutor.main(query)
def end():
    print("Programm wurde abgebrochen")
    sys.exit()
def completeend():
    print("Programm wurde beendet")
    sys.exit()
def invalidinput():
    print("Ihre Eingabe war invalide. Programm wird abgebrochen")
    sys.exit()

introduction = "Willkommen zur Feinstaubmessung! \n" \
               "Dieses Programm kann sich die Daten eines Feinstaub-Sensors und eines Temperatur-und-Luftfeuchtigkeits-Sensor von dem Archiv: https://archive.sensor.community/ holen, \n" \
               "diese in eine Datenbank importieren und SQL-Anfragen an der Datenbank ausführen. \n" \
               "Das Programm wird fragen, ob Sie die Funktionalität ausführen wollen oder nicht. \n" \
               "Sie können das Programm auch abbrechen, indem sie bei einer Frage anstatt 'y' oder 'n', 'stop' angeben. \n" \
               "Die Sensor-Daten werden in lokale CSV-Dateien geschrieben. \n" \
               "Bei jedem Datenbank Import werden die Daten des letzten Imports verloren. \n" \
               "Wenn Sie erneut eine SQL-Anfrage an die Datenbank machen wollen, müssen sie Daten nicht erneut holen und importieren. \n" \

print(introduction)

print("Sollen CSV-Daten der Sensoren geholt werden? y/n/stop")
answer = input()
if answer == 'stop':
    end()
if answer == 'y':
    print("Von wann sollen die CSV-Daten geholt werden?")
    print("Start-Datum(YYYY-MM-DD): ")
    startDate = input()
    print("End-Datum(YYYY-MM-DD): ")
    endDate = input()
    downloaddata(startDate, endDate)
    print("\nSollen die lokalen CSV-Daten in die Datenbank importiert werden? y/n/stop")
    answer2 = input()
    if answer2 == 'stop':
        end()
    if answer2 == 'y':
        importdata()
        print("\nWollen Sie eine SQL-Abfrage ausführen? y/n/stop")
        answer3 = input()
        if answer3 == 'stop':
            end()
        if answer3 == 'y':
            print("Welche Abfrage wollen Sie ausführen?\n 1. Maximale, Minimale und Durchschittliche Temperatur eines Tages\n 2. Maximale, Minimale und Durchschittliche Luftfeuchtigkeit eines Tages\n 3. Beide\n 1/2/3")
            sqlquery = input()
            print("Von wann sollen die Werte ausgegeben werden?")
            print("Datum(YYYY-MM-DD): ")
            date = input()
            querydb(date, sqlquery)
            completeend()
        if answer3 == 'n':
            completeend()
        else:
            invalidinput()
    if answer2 == 'n':
        print("\nWollen Sie eine SQL-Abfrage ausführen? y/n/stop")
        answer3 = input()
        if answer3 == 'stop':
            end()
        if answer3 == 'y':
            print("Welche Abfrage wollen Sie ausführen?\n 1. Maximale, Minimale und Durchschittliche Temperatur eines Tages\n 2. Maximale, Minimale und Durchschittliche Luftfeuchtigkeit eines Tages\n 3. Beide\n 1/2/3")
            sqlquery = input()
            print("Von wann sollen die Werte ausgegeben werden?")
            print("Datum(YYYY-MM-DD): ")
            date = input()
            querydb(date, sqlquery)
            completeend()
        if answer3 == 'n':
            completeend()
        else:
            invalidinput()
    else:
        end()
if answer == 'n':
    print("\nSollen die lokalen CSV-Daten in die Datenbank importiert werden? y/n/stop")
    answer2 = input()
    if answer2 == 'stop':
        end()
    if answer2 == 'y':
        importdata()
        print("\nWollen Sie eine SQL-Abfrage ausführen? y/n/stop")
        answer3 = input()
        if answer3 == 'stop':
            end()
        if answer3 == 'y':
            print("Welche Abfrage wollen Sie ausführen?\n 1. Maximale, Minimale und Durchschittliche Temperatur eines Tages\n 2. Maximale, Minimale und Durchschittliche Luftfeuchtigkeit eines Tages\n 3. Beide\n 1/2/3")
            sqlquery = input()
            print("Von wann sollen die Werte ausgegeben werden?")
            print("Datum(YYYY-MM-DD): ")
            date = input()
            querydb(date, sqlquery)
            completeend()
        if answer3 == 'n':
            completeend()
        else:
            invalidinput()
    if answer2 == 'n':
        print("\nWollen Sie eine SQL-Abfrage ausführen? y/n/stop")
        answer3 = input()
        if answer3 == 'stop':
            end()
        if answer3 == 'y':
            print("Welche Abfrage wollen Sie ausführen?\n 1. Maximale, Minimale und Durchschittliche Temperatur eines Tages\n 2. Maximale, Minimale und Durchschittliche Luftfeuchtigkeit eines Tages\n 3. Beide\n 1/2/3")
            sqlquery = input()
            print("Von wann sollen die Werte ausgegeben werden?")
            print("Datum(YYYY-MM-DD): ")
            date = input()
            querydb(date, sqlquery)
            completeend()
        if answer3 == 'n':
            completeend()
        else:
            invalidinput()
    else:
        invalidinput()
else:
    invalidinput()
