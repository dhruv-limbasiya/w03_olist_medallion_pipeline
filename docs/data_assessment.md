<!-- Customers -->

Dataset: Customers

Grain:
1 row = 1 order

Primary Key:
customer_id

Important Columns:
customer_id
customer_unique_id
customer_city
customer_state

Purpose:
Stores customer information and location.

<!-- orders -->

Grain:
1 row = 1 order

Primary Key:
order_id

Foreign Key:
customer_id

Important Columns:
order_id
customer_id
order_status
order_purchase_timestamp
order_delivered_customer_date

Purpose:
Tracks the complete order lifecycle.


<!-- order-item -->

Grain:
1 row = 1 item within an order

Primary Key:
(order_id, order_item_id)

Foreign Keys:
order_id
product_id
seller_id

Important Columns:
order_id
order_item_id
product_id
seller_id
price
freight_value

Purpose:
Stores products purchased within each order.

<!-- order-payment -->

Grain:
1 row = 1 payment transaction

Primary Key:
(order_id, payment_sequential)

Foreign Key:
order_id

Important Columns:
order_id
payment_type
payment_installments
payment_value

Purpose:
Stores payment information for orders.

<!-- order-review -->

Grain:
1 row = 1 customer review

Primary Key:
review_id

Foreign Key:
order_id

Important Columns:
review_id
order_id
review_score
review_comment_message

Purpose:
Stores customer feedback and ratings.


<!-- products -->

Grain:
1 row = 1 product

Primary Key:
product_id

Foreign Key:
product_category_name

Important Columns:
product_id
product_category_name
product_weight_g
product_length_cm
product_width_cm
product_height_cm

Purpose:
Stores product master information.

<!-- sellers -->

Grain:
1 row = 1 seller

Primary Key:
seller_id

Important Columns:
seller_id
seller_city
seller_state

Purpose:
Stores seller information and location.

<!-- geolocation -->
Grain:
1 row = 1 geolocation record

Primary Key:
No obvious primary key

Important Columns:
geolocation_zip_code_prefix
geolocation_lat
geolocation_lng
geolocation_city
geolocation_state

Purpose:
Maps zip codes to geographic coordinates.

<!-- category-transaction -->
Grain:
1 row = 1 category translation

Primary Key:
product_category_name

Important Columns:
product_category_name
product_category_name_english

Purpose:
Maps Portuguese product categories to English categories.