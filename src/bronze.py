import pandas as pd 
from datetime import datetime 

def bronzeLayer(df, file_path):
    df["_ingesion_timestamp"] = datetime.now()
    
    df["Source_file"] = file_path
    
    return df

def save_bronze(df, output_path):

    df.to_csv(output_path, index=False)