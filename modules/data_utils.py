import pandas as pd
from sklearn.cluster import KMeans
import streamlit as st

def clean_numeric(value):
    if isinstance(value, str):
        return float(''.join(filter(lambda x: x.isdigit() or x == '.', value)))
    return value

@st.cache_data
def load_and_prepare_data():
    data = pd.read_excel('data/nutrition.xlsx')
    numeric_columns = ['calories', 'protein', 'carbohydrate', 'total_fat', 'fiber']
    for col in numeric_columns:
        data[col] = data[col].apply(clean_numeric)

    kmeans = KMeans(n_clusters=3, random_state=42)
    data['meal_type'] = kmeans.fit_predict(data[['calories', 'protein', 'carbohydrate', 'total_fat']])
    cluster_map = dict(enumerate(['breakfast', 'lunch', 'dinner']))
    data['meal_type'] = data['meal_type'].map(cluster_map)
    return data
