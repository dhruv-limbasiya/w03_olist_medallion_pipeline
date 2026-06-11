# Olist Medallion Architecture Pipeline

## Project Overview

This project implements a Medallion Architecture pipeline using the Olist Brazilian E-Commerce Dataset.

The pipeline transforms raw e-commerce data into analytics-ready business datasets using Bronze, Silver, and Gold layers.

---

## Architecture

Raw Layer
↓
Bronze Layer
↓
Silver Layer
↓
Gold Layer

---

## Technologies Used

- Python
- Pandas
- CSV
- Logging
- Data Validation
- Medallion Architecture

---

## Project Structure

data/
├── raw/
├── bronze/
├── silver/
└── gold/

src/
├── extract.py
├── bronze.py
├── silver.py
├── gold.py
├── validations.py
└── main.py

docs/
├── data_assessment.md
├── relationship_diagram.md
├── medallion_architecture.md
├── data_quality_rules.md
└── business_report.md

---

## Bronze Layer

Purpose:

Store source data with ingestion metadata.

Added Columns:

- _ingestion_timestamp
- _source_file

---

## Silver Layer

Purpose:

Create trusted datasets through validation and standardization.

Examples:

- Datetime conversion
- Data validation
- Text standardization

---

## Gold Layer

Business-ready datasets:

- customer_revenue.csv
- product_revenue.csv
- monthly_revenue.csv
- state_revenue.csv
- order_summary.csv

---

## Business Questions Answered

- Top customers by revenue
- Top products by revenue
- Revenue by state
- Monthly revenue trend
- Order-level revenue analysis