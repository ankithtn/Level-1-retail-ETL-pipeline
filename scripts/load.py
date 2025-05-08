import psycopg2
import pandas as pd
import os  
from dotenv import load_dotenv

load_dotenv()

def load_data_to_postgres(csv_path):
    #Load cleaned csv
    df = pd.read_csv(csv_path)

    # Rename columns to match postgres table or schema
    df.rename(columns={
        "Row ID": "row_id",
        "Order ID": "order_id",
        "Order Date": "order_date",
        "Ship Date": "ship_date",
        "Ship Mode": "ship_mode",
        "Customer ID": "customer_id",
        "Customer Name": "customer_name",
        "Segment": "segment",
        "Country": "country",
        "City": "city",
        "State": "statee",  
        "Postal Code": "postal_code",
        "Region": "region",
        "Product ID": "product_id",
        "Category": "category",
        "Sub-Category": "sub_category",
        "Product Name": "product_name",
        "Sales": "sales",
        "Quantity": "quantity",
        "Discount": "discount",
        "Profit": "profit"
    }, inplace=True)

    conn = None # define upfront for exception handling

    try:
        # Establish Connection
        conn = psycopg2.connect(
            dbname = os.getenv("DB_NAME"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            host = os.getenv("DB_HOST"),
            port = os.getenv("DB_PORT")
        )
        cur = conn.cursor()

        # Parameterized insert query
        insert_query = """
            INSERT INTO superstore (
                row_id, order_id, order_date, ship_date, ship_mode,
                customer_id, customer_name, segment, country, city,
                statee, postal_code, region, product_id, category,
                sub_category, product_name, sales, quantity, discount, profit
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        for _, row in df.iterrows():
            cur.execute(insert_query, (
                int(row["row_id"]),
                row["order_id"],
                row["order_date"],
                row["ship_date"],
                row["ship_mode"],
                row["customer_id"],
                row["customer_name"],
                row["segment"],
                row["country"],
                row["city"],
                row["statee"],
                str(row["postal_code"]) if not pd.isna(row["postal_code"]) else None,
                row["region"],
                row["product_id"],
                row["category"],
                row["sub_category"],
                row["product_name"],
                row["sales"],
                row["quantity"],
                row["discount"],
                row["profit"]
            ))
            
        conn.commit()
        print("Data loaded successfully into PostgreSQL.")
    
    except psycopg2.Error as e:
        print("Error while loading data:", e)
        if conn:
            conn.rollback()
    
    finally:
        if conn:
            cur.close()
            conn.close()

if __name__ == "__main__":
    load_data_to_postgres("data/processed/cleaned_data.csv")