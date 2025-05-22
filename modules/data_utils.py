# Import pandas for data manipulation
import pandas as pd
# Import KMeans clustering algorithm from scikit-learn
from sklearn.cluster import KMeans
# Import Streamlit for building the web interface
import streamlit as st
# Function to clean numeric data by removing unwanted characters from strings (like 'g', 'kcal', etc.)
def clean_numeric(value):
     # If the value is a string, remove everything except digits and decimal point
    if isinstance(value, str):
        return float(''.join(filter(lambda x: x.isdigit() or x == '.', value)))
    return value     # If it's already numeric, return as-is
# Cache the result of this function so it doesn't rerun on every page refresh
@st.cache_data
def load_and_prepare_data():
     # Load data from an Excel file located in the 'data' folder
    data = pd.read_excel('data/nutrition.xlsx')
    # List of columns we want to clean (expected to contain numeric values)
    numeric_columns = ['calories', 'protein', 'carbohydrate', 'total_fat', 'fiber']
     # Apply the clean_numeric function to each value in each numeric column
    for col in numeric_columns:
        data[col] = data[col].apply(clean_numeric)
     # Apply KMeans clustering on selected nutritional columns to categorize meals
    kmeans = KMeans(n_clusters=3, random_state=42)  # Create KMeans object with 3 clusters
    data['meal_type'] = kmeans.fit_predict(data[['calories', 'protein', 'carbohydrate', 'total_fat']])
    # The 'meal_type' column now contains cluster labels: 0, 1, or 2
    
    # Map those cluster numbers to actual meal names
    cluster_map = dict(enumerate(['breakfast', 'lunch', 'dinner']))  # You can change order if needed
    data['meal_type'] = data['meal_type'].map(cluster_map)  # Replace 0,1,2 with names
    
    # Return the cleaned and enriched dataset
    return data
