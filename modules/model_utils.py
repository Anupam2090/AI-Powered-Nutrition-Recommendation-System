from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from joblib import dump, load
import os

def train_random_forest(data):
    features = ['calories', 'protein', 'carbohydrate', 'total_fat', 'fiber']
    X = data[features]
    y = (data['calories'] > data['calories'].mean()).astype(int)

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    y_pred = rf_model.predict(X)
    metrics = {
        'accuracy': accuracy_score(y, y_pred),
        'precision': precision_score(y, y_pred),
        'recall': recall_score(y, y_pred),
        'f1': f1_score(y, y_pred),
    }

    dump(rf_model, 'models/rf_model.joblib')
    return rf_model, y_pred, metrics

def load_or_train_model(data):
    if os.path.exists('models/rf_model.joblib'):
        return load('models/rf_model.joblib')
    rf_model, _, _ = train_random_forest(data)
    return rf_model
