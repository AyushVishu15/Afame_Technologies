# G:\Afame Technologies\src\model_training.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
from data_preprocessing import load_and_clean_data
from utils import save_metrics
import os

def train_model():
    try:
        print("Script started: model_training.py")
        X, y, _, _ = load_and_clean_data('G:/Afame Technologies/data/movie_dataset.csv')
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        r2 = r2_score(y_test, y_pred)
        
        save_metrics(rmse, r2, '../results/model_performance.txt')
        
        os.makedirs('../models', exist_ok=True)
        joblib.dump(model, '../models/movie_rating_model.pkl')
        print(f"Model saved to '../models/movie_rating_model.pkl'")
        
        return model, rmse, r2
    
    except Exception as e:
        print(f"Error in model training: {e}")
        raise

if __name__ == "__main__":
    model, rmse, r2 = train_model()
    print(f"Model trained successfully. RMSE: {rmse:.4f}, R2: {r2:.4f}")