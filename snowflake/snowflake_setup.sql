-- Create database and schema
CREATE OR REPLACE DATABASE ECOMMERCE_DB;
USE DATABASE ECOMMERCE_DB;

CREATE OR REPLACE SCHEMA PUBLIC;
USE SCHEMA PUBLIC;

-- Create predictions table
CREATE OR REPLACE TABLE predictions (
    CustomerID INT,
    Quantity FLOAT,
    year INT,
    month INT,
    PredictedPrice FLOAT
);

-- Create stage for CSV loading
CREATE OR REPLACE STAGE predictions_stage;

-- Load predictions CSV
COPY INTO predictions
FROM @predictions_stage
FILE_FORMAT = (
    TYPE = 'CSV'
    SKIP_HEADER = 1
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    ERROR_ON_COLUMN_COUNT_MISMATCH = FALSE
);
