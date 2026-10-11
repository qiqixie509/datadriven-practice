CREATE TABLE dim_plate (
    id VARCHAR,
    plate_number VARCHAR,
    PRIMARY KEY (id)
);

CREATE TABLE dim_section (
    id VARCHAR,
    name VARCHAR,
    PRIMARY KEY (id)
);

CREATE TABLE fact_commuter (
    event_id VARCHAR,
    plate_id VARCHAR,
    section_id VARCHAR,
    event_type VARCHAR,
    event_time TIMESTAMP,
    PRIMARY KEY (event_id)
);

ALTER TABLE fact_commuter
    ADD FOREIGN KEY (plate_id) REFERENCES dim_plate (id);

ALTER TABLE fact_commuter
    ADD FOREIGN KEY (section_id) REFERENCES dim_section (id);
