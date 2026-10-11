CREATE TABLE dim_seller (
    id VARCHAR,
    name VARCHAR,
    gender VARCHAR,
    email VARCHAR,
    phone VARCHAR,
    PRIMARY KEY (id)
);

CREATE TABLE dim_products (
    name VARCHAR,
    id VARCHAR,
    price DECIMAL,
    PRIMARY KEY (id)
);

CREATE TABLE fact_sale (
    quantity INT,
    product_id VARCHAR,
    id VARCHAR,
    total_amount DECIMAL,
    created_at TIMESTAMP,
    sale_date DATE,
    PRIMARY KEY (id)
);

CREATE TABLE new_table (
);

CREATE TABLE fact_list (
    product_id VARCHAR,
    seller_id VARCHAR,
    active BOOLEAN,
    update_at TIMESTAMP,
    went_live_date DATE
);

ALTER TABLE fact_list
    ADD FOREIGN KEY (seller_id) REFERENCES dim_seller (id);

ALTER TABLE fact_sale
    ADD FOREIGN KEY (product_id) REFERENCES fact_list (product_id);

ALTER TABLE fact_sale
    ADD FOREIGN KEY (product_id) REFERENCES dim_products (id);
