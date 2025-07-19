CREATE TABLE meetings (
    circuit_key INT NOT NULL,
    circuit_short_name VARCHAR(100) NOT NULL,
    country_code CHAR(3) NOT NULL,
    country_name VARCHAR(100) NOT NULL,
    date_start TIMESTAMP NOT NULL,
    gmt_offset VARCHAR(9) NOT NULL,
    location VARCHAR(100) NOT NULL,
    meeting_code CHAR(3) NOT NULL,
    meeting_key INT NOT NULL,
    meeting_name VARCHAR(100) NOT NULL,
    meeting_official_name VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    PRIMARY KEY (meeting_key)
);