import pandas as pd 

df = pd.read_csv("data/processed/cleaned_data.csv", parse_dates=["Order Date", "Ship Date"])

print(df.dtypes)