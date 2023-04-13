CREATE TABLE IF NOT EXISTS tempandhumid (
    tempandhumid_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_id INT,
    sensor_type TEXT,
    location INT,
    lat INT,
    lon INT,
    timestamp TEXT,
    temperature REAL,
    humidity REAL
);