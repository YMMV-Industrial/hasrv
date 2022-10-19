
DROP TABLE IF EXISTS iostate;

CREATE TABLE iostate (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ioname TEXT NOT NULL,
    iodesc TEXT,
    iostate INT
);