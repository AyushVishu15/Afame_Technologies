# G:\Afame Technologies\test_file.py
import pandas as pd
df = pd.read_csv('data/movie dataset.csv', encoding='latin1')
print("File found! Columns:", df.columns.tolist())