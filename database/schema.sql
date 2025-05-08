CREATE table superstore (
    row_id SERIAL PRIMARY KEY,
    order_id VARCHAR,
    order_date DATE,
    ship_date DATE,
    ship_mode VARCHAR,
    customer_id VARCHAR,
    customer_name VARCHAR,
    segment VARCHAR,
    country VARCHAR,
    city VARCHAR,
    statee VARCHAR,
    postal_code VARCHAR,
    region VARCHAR,
    product_id VARCHAR,
    catergory VARCHAR,
    sub_category VARCHAR,
    product_name  TEXT,
    sales NUMERIC,
    quantity INTEGER,
    discount NUMERIC,
    profit NUMERIC
);

ALTER table superstore rename column catergory to category;