import pandas as pd

def clean_data(file_path: str, output_path: str):
    df = pd.read_csv(file_path, encoding='iso-8859-1')

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Strip whitespace from column names and categorical fields
    df.columns = df.columns.str.strip()
    categorical_cols = ["Region", "Segment", "Category", "Sub-Category", "Ship Mode"]
    for col in categorical_cols:
        df[col] = df[col].str.strip().str.title()

    # Convert date columns
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

    # Check the conversion result
    print(df[["Order Date", "Ship Date"]].dtypes)

    # Save cleaned data
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to: {output_path}")

if __name__ == "__main__":
    clean_data("data/raw/Superstore.csv", "data/processed/cleaned_data.csv")
