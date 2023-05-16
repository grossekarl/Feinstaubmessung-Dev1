# Feinstaubmessung Dev 1.7
## Beschreibung
* holt sich die Roh-Daten von den Sensoren SDS011 und DHT22 von einem online Archiv
* diese werde in ihren eigenen CSV-Dateien geschrieben
* die CSV-Dateien können in eine Datenbank importiert werden
* es können SQL-Abfragen an der Datenbank ausgeführt werden
## Ausführung
* in Konsole
* Befehl: python3 PythonPrograms/run.py
## Funktionalität
* Es können Roh-Daten geholt werden, welche dann in CSV-Dateien geschrieben werden
  * es wird eine Eingabe von einem Start und End-Datum für den Zeitraum der Daten erwartet
* Die CSV-Dateien können in die DB importiert werden
* Man kann an einer Auswahl von vorgefertigten SQL-Abfragen eine ausführen
  * Derzeit 4 mögliche Abfragen
  * Die Abfragen holen die Minimal, Maximal und Durchschnittswerte eines Tages
    * Der Tag muss als Datum angegeben werden
* Bei jeder Aktion kann man angeben, ob man sie ausführen, nicht ausführen oder das Programm beenden will (nicht bei Datum Angabe)
