import pandas as pd

# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

def load_dataset(path: str, encoding: str = "iso-8859-1") -> pd.DataFrame:
    """Loads the dataset from the given path."""
    return pd.read_csv(path, encoding=encoding)

def inspect_structure(df: pd.DataFrame):
    """Prints structure and basic info of the DataFrame."""
    print("\n--- Head (First 10 Rows) ---")
    print(df.head(10))

    print("\n--- Info ---")
    print(df.info())

    print("\n--- Shape ---")
    print(df.shape)

    print("\n--- Describe ---")
    print(df.describe(include='all'))

    print("\n--- Data Types ---")
    print(df.dtypes)

def check_missing_duplicates(df: pd.DataFrame):
    """Prints missing and duplicate values."""
    print("\n--- Null Values (BOOLEAN) ---")
    print(df.isnull())

    print("\n--- Null Value Count ---")
    print(df.isnull().sum())

    print("\n--- Duplicates (Boolean) ---")
    print(df.duplicated())

    print("\n--- Duplicate row count ---")
    print(df.duplicated().sum())

if __name__ == "__main__":
    file_path = "data/raw/Superstore.csv"
    df = load_dataset("data/raw/Superstore.csv")

    inspect_structure(df)
    check_missing_duplicates(df)
