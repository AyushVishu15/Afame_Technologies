
import pandas as pd

def read_csv_with_encoding(file_path):
    encodings = ['utf-8', 'latin1', 'iso-8859-1', 'cp1252']
    for encoding in encodings:
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            print(f"Success! File read with encoding: {encoding}")
            print("Dataset columns:", df.columns.tolist())
            print("\nFirst 5 rows:")
            print(df.head())
            return df
        except Exception as e:
            print(f"Failed with encoding {encoding}: {e}")
    raise ValueError("Could not read file with any tested encoding.")

if __name__ == "__main__":
    try:
        df = read_csv_with_encoding('data/movie dataset.csv')
    except Exception as e:
        print(f"Error: {e}")
