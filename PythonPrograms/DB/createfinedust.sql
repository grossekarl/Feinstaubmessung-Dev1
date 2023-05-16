CREATE TABLE IF NOT EXISTS finedust (
    'finedust_id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'sensor_id' INT,
    'sensor_type' TEXT,
    'location' INT,
    'lat' REAL,
    'lon' REAL,
    'timestamp' DATETIME,
    'P1' REAL,
    'durP1' REAL,
    'ratioP1' REAL,
    'P2' REAL,
    'durP2' REAL,
    'ratioP2' REAL
);