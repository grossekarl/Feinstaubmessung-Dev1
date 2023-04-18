# Feinstaubmessung Dev 1.7
## Beschreibung
* holt sich die Roh-Daten von den Sensoren SDS011 und DHT22 und schreibt eine CSV für beide
* Terminal: py PythonPrograms/main.py [Start-Datum in YYYY-MM-DD Format] [End-Datum in YYYY-MM-DD Format]
* Angabe der Sensoren, von denen Daten gesammelt werden
## Funktionalität
* Information abrufen, um zu schauen wie das Wetter vorher war
* CSV Dateien werden in DB importiert
* Abfrage ob die Daten aktualisiert werden sollen
* User kann zwischen zwei SQL-Abfragen auswählen
* Werte werden ausgegeben
