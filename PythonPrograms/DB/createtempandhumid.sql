CREATE TABLE IF NOT EXISTS tempandhumid (
    'tempandhumid_id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'sensor_id' INT,
    'sensor_type' TEXT,
    'location' INT,
    'lat' REAL,
    'lon' REAL,
    'timestamp' DATETIME,
    'temperature' REAL,
    'humidity' REAL
);