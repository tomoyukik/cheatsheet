CREATE TABLE IF NOT EXISTS history (
    datetime TIMESTAMP PRIMARY KEY
    , number INT
);

INSERT INTO history
VALUES (NOW(), 345);
