# Medallion Architecture

## Project Overview

This project implements a Medallion Architecture pipeline using the Olist Brazilian E-Commerce Dataset.

The objective is to transform raw e-commerce data into analytics-ready business datasets using Bronze, Silver, and Gold layers.

---

## Architecture Flow

Raw Layer
↓
Bronze Layer
↓
Silver Layer
↓
Gold Layer

---

## Raw Layer

Purpose:

Store source CSV files exactly as received.

Datasets:

* customers
* orders
* order_items
* products
* sellers
* payments
* reviews
* geolocation
* category_translation

No transformations are performed.

---

## Bronze Layer

Purpose:

Create a historical copy of source data and capture ingestion metadata.

Transformations:

* Add _ingestion_timestamp
* Add _source_file

No business transformations are performed.

---

## Silver Layer

Purpose:

Create trusted and standardized datasets.

Transformations:

* Datetime conversion for order dates
* Data quality validation
* Standardization of text fields
* Removal of Bronze metadata columns

Validation Examples:

* order_id cannot be null
* customer_id cannot be null
* product_id cannot be null
* seller_id cannot be null

---

## Gold Layer

Purpose:

Create business-ready datasets for analytics.

Gold Outputs:

* gold_customer_revenue
* gold_product_revenue
* gold_monthly_revenue
* gold_state_revenue
* gold_order_summary

These datasets are optimized for reporting and business analysis.
