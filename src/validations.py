def validate_orders(df):

    if df["order_id"].isnull().sum() > 0:
        raise ValueError("order_id contains null values")

    if df["customer_id"].isnull().sum() > 0:
        raise ValueError("customer_id contains null values")

    if df["order_id"].duplicated().sum() > 0:
        raise ValueError("duplicate order_id found")


def validate_customers(df):

    if df["customer_id"].isnull().sum() > 0:
        raise ValueError("customer_id contains null values")

    if df["customer_unique_id"].isnull().sum() > 0:
        raise ValueError("customer_unique_id contains null values")


def validate_products(df):

    if df["product_id"].isnull().sum() > 0:
        raise ValueError("product_id contains null values")


def validate_sellers(df):

    if df["seller_id"].isnull().sum() > 0:
        raise ValueError("seller_id contains null values")