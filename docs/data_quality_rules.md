# Data Quality Rules

## Orders

Rules:

* order_id must not be null
* customer_id must not be null
* order_id must be unique

Reason:

Required to uniquely identify each order.

---

## Customers

Rules:

* customer_id must not be null
* customer_unique_id must not be null

Reason:

Required for customer-level analysis.

---

## Products

Rules:

* product_id must not be null

Reason:

Required for product analytics.

---

## Sellers

Rules:

* seller_id must not be null

Reason:

Required for seller-level reporting.

---

## Silver Layer Transformations

Orders:

* Convert timestamps to datetime format

Customers:

* Standardize city names

Sellers:

* Standardize city names

Category Translation:

* Standardize category names
