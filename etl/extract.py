import pandas as pd

def from_csv(filepath):
    print("Extracting data...")
    return pd.read_csv(filepath)
