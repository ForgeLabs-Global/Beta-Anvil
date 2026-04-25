import pandas as pd

def load_data(path):
    """Loading the CSV file into a Pandas DataFrame."""
    return pd.read_csv(path)

def clean_data(df):
    """Applies all data cleaning steps."""
    # Drop any duplicate rows
    df = df.drop_duplicates()
    
    # Standardize column headers (replace spaces/slashes with underscores)
    df.columns = df.columns.str.replace(' ', '_').str.replace('/', '_').str.lower()
    
    return df

def save_data(df, path):
    """Saving the cleaned DataFrame to the specified path."""
    df.to_csv(path, index=False)
