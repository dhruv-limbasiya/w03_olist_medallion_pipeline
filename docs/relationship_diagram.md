# Relationship Diagram

Customers (1) -------- (M) Orders

Orders (1) -------- (M) Order Items

Products (1) -------- (M) Order Items

Orders (1) -------- (M) Payments

Orders (1) -------- (1) Reviews

Sellers (1) -------- (M) Order Items

Product Category Translation (1) -------- (M) Products

Relationship Keys:

customers.customer_id
→ orders.customer_id

orders.order_id
→ order_items.order_id

products.product_id
→ order_items.product_id

orders.order_id
→ payments.order_id

orders.order_id
→ reviews.order_id

sellers.seller_id
→ order_items.seller_id
