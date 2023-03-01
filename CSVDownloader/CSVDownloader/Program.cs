using System;
using System.Collections.Generic;
using System.IO;
using System.Net;

namespace CSVDownloader
{
    class Program
    {
        static void Main(string[] args)
        {
            // URL der Sensor Community Daten
            string url = "http://archive.sensor.community/";

            // Start- und Enddatum des gewünschten Zeitraums
            DateTime startDate = new DateTime(2022, 1, 1);
            DateTime endDate = new DateTime(2023, 2, 21);

            // Sensor IDs
            string sensorIdsString = "3659,3660";

            // Sensor IDs in eine Liste von Integern umwandeln
            List<int> sensorIds = new List<int>();
            foreach (string sensorIdString in sensorIdsString.Split(','))
            {
                if (int.TryParse(sensorIdString, out int sensorId))
                {
                    sensorIds.Add(sensorId);
                }
            }


            // Pfad zur CSV-Datei
            string csvFilePath = @"/home/oem/Dekstop/TBS1/Git-Arbeit/Test/Import.csv";

            // CSV-Datei öffnen
            StreamWriter csvFile = new StreamWriter(csvFilePath);

            // Schreibe die Spaltenüberschriften in die CSV-Datei
            csvFile.WriteLine("Sensor_ID;sensor_type;Location;Lat;Lon;Timestamp;P1;P2;Temperature;Humidity");

            // Durchlaufe alle Tage im Zeitraum
            for (DateTime date = startDate; date <= endDate; date = date.AddDays(1))
            {
                // URL für das aktuelle Datum
                string dateUrl = url + date.ToString("yyyy-MM-dd") + "/";

                // Durchlaufe alle Sensor IDs
                foreach (int sensorId in sensorIds)
                {
                    // URL für das jeweilige CSV
                    string csvUrl = dateUrl + date.ToString("yyyy-MM-dd") + GetSensorName(sensorId) + ".csv";

                    try
                    {
                        // Webanfrage erstellen
                        WebRequest request = WebRequest.Create(csvUrl);
                        WebResponse response = request.GetResponse();
                        Stream dataStream = response.GetResponseStream();

                        // Lesen der CSV-Daten
                        StreamReader reader = new StreamReader(dataStream);
                        //reader.ReadLine();
                        // Die erste Zeile der CSV enthält die Spaltenüberschriften und wird übersprungen
                        string csvContent = reader.ReadLine();
                        while (!reader.EndOfStream)
                        {
                            string line = reader.ReadLine();
                            string[] values = line.Split(';');

                            // Überprüfe, ob die Zeile die richtige Sensor ID enthält
                            if (values.Length > 0 && int.TryParse(values[0], out int lineSensorId) && lineSensorId == sensorId)
                            {
                                // Erstelle die neue Zeile mit den angepassten Spaltenwerten
                                string newLine = lineSensorId + ";" +
                                    (values.Length > 1 ? values[1] : "") + ";" +
                                    (values.Length > 2 ? values[2] : "") + ";" +
                                    (values.Length > 3 ? values[3] : "") + ";" +
                                    (values.Length > 4 ? values[4] : "") + ";" +
                                    (values.Length > 5 ? values[5] : "") + ";" +
                                    (sensorId == 3659 && values.Length > 6 ? (values[6] != "" ? values[6] : "") : "") + ";" +
                                    (sensorId == 3659 && values.Length > 9 ? (values[9] != "" ? values[9] : "") : "") + ";" +
                                    (sensorId == 3660 && values.Length > 6 ? (values[6] != "" ? values[6] : "") : "") + ";" +
                                    (sensorId == 3660 && values.Length > 7 ? (values[7] != "" ? values[7] : "") : "");

                                // Schreibe die neue Zeile in die CSV-Datei
                                csvFile.WriteLine(newLine);
                            }
                        }
                        Console.WriteLine($"CSV-Datei für Sensor {sensorId} am {date.ToString("yyyy-MM-dd")} heruntergeladen und gespeichert.");
                    }
                    catch (WebException)
                    {
                        Console.WriteLine($"CSV-Datei für Sensor {sensorId} am {date.ToString("yyyy-MM-dd")} konnte nicht heruntergeladen werden.");
                    }
                }
            }

            // CSV-Datei schließen
            csvFile.Close();

            Console.WriteLine("Alle CSV-Dateien wurden erfolgreich heruntergeladen und in die Datei geschrieben.");
            Console.ReadLine();
        }

        static string GetSensorName(int sensorId)
        {
            // Mapping von Sensor IDs zu Namen
            switch (sensorId)
            {
                case 3659:
                    return "_sds011_sensor_3659";
                case 3660:
                    return "_dht22_sensor_3660";
                default:
                    throw new ArgumentException($"Unbekannte Sensor ID: {sensorId}");
            }
        }
    }
}
