CREATE SCHEMA IF NOT EXISTS retail;

CREATE TABLE IF NOT EXISTS retail.online_retail_raw (
    "InvoiceNo" VARCHAR,
    "StockCode" VARCHAR,
    "Description" VARCHAR,
    "Quantity" INTEGER,
    "InvoiceDate" DATE,
    "UnitPrice" REAL,
    "CustomerID" VARCHAR,
    "Country" VARCHAR
);
