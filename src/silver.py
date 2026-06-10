import pandas as pd


def clean_orders(df):

    date_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]

    for col in date_columns:

        if col in df.columns:

            df[col] = pd.to_datetime(
                df[col],
                errors="coerce"
            )

    return df


def clean_customers(df):

    if "customer_city" in df.columns:

        df["customer_city"] = (
            df["customer_city"]
            .str.strip()
            .str.lower()
        )

    return df


def clean_sellers(df):

    if "seller_city" in df.columns:

        df["seller_city"] = (
            df["seller_city"]
            .str.strip()
            .str.lower()
        )

    return df


def clean_category_translation(df):

    translation_columns = [
        "product_category_name",
        "product_category_name_english"
    ]

    for col in translation_columns:

        if col in df.columns:

            df[col] = (
                df[col]
                .str.strip()
                .str.lower()
            )

    return df


def silver_layer(df, dataset_name):

    bronze_cols = [
        "_ingestion_timestamp",
        "_source_file"
    ]

    df = df.drop(
        columns=[
            col for col in bronze_cols
            if col in df.columns
        ],
        errors="ignore"
    )

    if dataset_name == "orders":
        return clean_orders(df)

    elif dataset_name == "customers":
        return clean_customers(df)

    elif dataset_name == "sellers":
        return clean_sellers(df)

    elif dataset_name == "category_translation":
        return clean_category_translation(df)

    return df


def save_silver(df, output_path):

    df.to_csv(
        output_path,
        index=False
    )