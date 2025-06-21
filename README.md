# Movie Rating Prediction

A machine learning application to predict movie ratings based on features like genre, director, and actors using an IMDb dataset of Indian movies. 

## Project Overview
- **Objective**: Develop a regression model to predict movie ratings using features such as genre, director, and actors.
- **Dataset**: Indian movies dataset (`data/movie_dataset.csv`) from IMDb, preprocessed to handle missing values and encode categorical features.
- **Technologies**: Python, Pandas, Scikit-learn, Matplotlib, Seaborn, Jupyter Notebook.
- **Model**: Random Forest Regressor.
- **Outputs**: Preprocessed dataset, trained model, performance metrics (RMSE, R²), and visualizations (rating distribution, genre vs. rating).


## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/AyushVishu15/Movie_Rating_Predictor.git
   cd Movie_Rating_Predictor

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
4. Run the project:
    ```bash
   python src/run_all.py


## Screenshots
Rating Distribution Plot
![image](https://github.com/user-attachments/assets/630b26bc-8f49-4722-9243-436323176c07)

Genre vs. Rating Plot
![image](https://github.com/user-attachments/assets/4fbb4980-d350-4309-8264-99817ea9255b)
