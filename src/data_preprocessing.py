# G:\Afame Technologies\src\data_preprocessing.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import os

def load_and_clean_data(file_path='G:/Afame Technologies/data/movie_dataset.csv', encoding='latin1'):
    try:
        print("Script started: data_preprocessing.py")
        abs_path = os.path.abspath(file_path)
        print(f"Attempting to load file: {abs_path}")
        df = pd.read_csv(abs_path, encoding=encoding)
        print("Dataset columns:", df.columns.tolist())
        
        rating_col = 'Rating'
        if rating_col not in df.columns:
            raise ValueError(f"'{rating_col}' column not found in dataset")
        
        df = df.dropna(subset=[rating_col])
        categorical_cols = ['Genre', 'Director', 'Actor 1', 'Actor 2', 'Actor 3']
        for col in categorical_cols:
            if col in df.columns:
                df[col] = df[col].fillna('Unknown')
            else:
                print(f"Warning: Column {col} not found")
        
        le_dict = {}
        for col in categorical_cols:
            if col in df.columns:
                le = LabelEncoder()
                df[f'{col}_encoded'] = le.fit_transform(df[col].astype(str))
                le_dict[col] = le
        
        feature_cols = [col for col in df.columns if '_encoded' in col]
        if not feature_cols:
            raise ValueError("No encoded features found. Check categorical columns.")
        
        X = df[feature_cols]
        y = df[rating_col]
        
        output_path = 'G:/Afame Technologies/data/cleaned_movie_dataset.csv'
        print(f"Attempting to save cleaned dataset to: {output_path}")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        if os.path.exists(output_path):
            print(f"Cleaned dataset successfully saved to {output_path}")
        else:
            print(f"Failed to save cleaned dataset to {output_path}")
        
        return X, y, df, le_dict
    
    except Exception as e:
        print(f"Error in preprocessing: {e}")
        raise

if __name__ == "__main__":
    X, y, df, _ = load_and_clean_data()