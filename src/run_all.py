
import os

print("Running preprocessing...")
os.system("python src/data_preprocessing.py")
print("Running model training...")
os.system("python src/model_training.py")
print("Please open and run 'notebooks/movie_rating_prediction.ipynb' in VS Code for EDA.")
