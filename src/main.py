from extract import extract
from bronze import bronzeLayer, save_bronze
import logging as log

log.basicConfig(
    filename="logs/pipeline.log",
    level=log.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


files = [
    ("./data/raw/olist_customers_dataset.csv",
     "olist_customers_dataset.csv",
     "./data/bronze/bronze_customers.csv" 
     ),
    
    ("./data/raw/olist_geolocation_dataset.csv",
    "olist_geolocation_dataset.csv",
    "./data/bronze/bronze_geolocation.csv"
     ),
    
    ("./data/raw/olist_order_items_dataset.csv",
     "olist_order_items_dataset.csv",
     "./data/bronze/bronze_order_items.csv"
     ),
    
    ("./data/raw/olist_order_payments_dataset.csv",
     "olist_order_payments_dataset.csv",
     "./data/bronze/bronze_order_payments.csv"
     ),
    
    ("./data/raw/olist_order_reviews_dataset.csv",
     "olist_order_reviews_dataset.csv",
     "./data/bronze/bronze_order_reviews.csv"
     ),
    
    ("./data/raw/olist_orders_dataset.csv",
     "olist_orders_dataset.csv",
     "./data/bronze/bronze_orders.csv"
     ),
    
    ("./data/raw/olist_products_dataset.csv",
     "olist_products_dataset.csv",
     "./data/bronze/bronze_products.csv"
     ),
    
    ("./data/raw/olist_sellers_dataset.csv",
     "olist_sellers_dataset.csv",
     "./data/bronze/bronze_sellers.csv"
     ),
    
    ("./data/raw/product_category_name_translation.csv",
     "product_category_name_translation.csv",
     "./data/bronze/bronze_product_category_name_translation.csv"
     )
]

log.info("Bronze Pipeline Started")

for raw_path, source_file, bronze_path in files:
    try:
            df = extract(raw_path)
            
            log.info(f"{source_file} -> Rows: {len(df)}")
            
            df = bronzeLayer(df,source_file)
            
            save_bronze(df,bronze_path)
        
            log.info( f"{source_file} processed successfully")
        
    except Exception as e:
        log.error(f"Failed loading {source_file}: {e}" )
        
        
log.info("Bronze Pipeline Completed")        