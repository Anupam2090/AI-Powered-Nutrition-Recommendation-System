from sklearn.ensemble import RandomForestClassifier # Random Forest model
from sklearn.model_selection import train_test_split     # For splitting the dataset
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score # Evaluation metrics
from joblib import dump, load                        # For saving/loading model
import os                   # To check if the model file exists

# Function to train a Random Forest model on the nutrition dataset
def train_random_forest(data):
    # Define the input features (X) we will use for prediction
    features = ['calories', 'protein', 'carbohydrate', 'total_fat', 'fiber']
    X = data[features]
     # Define the target variable (y): 1 if calories are above average, else 0
    y = (data['calories'] > data['calories'].mean()).astype(int)

     # Split data into training and (ignored) test sets. We only train for now.
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
     
     # Create the Random Forest classifier with 100 decision trees
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Train the model using the training data
    rf_model.fit(X_train, y_train)
    
     # Predict using the full dataset for metric evaluation (not best practice but fine for simple use)
    y_pred = rf_model.predict(X)
    
     # Calculate evaluation metrics
    metrics = {
        'accuracy': accuracy_score(y, y_pred),   # % of correct predictions
        'precision': precision_score(y, y_pred),  # True positives / Predicted positives
        'recall': recall_score(y, y_pred),       # True positives / Actual positives
        'f1': f1_score(y, y_pred),               # Harmonic mean of precision and recall
    }
    
 # Save the trained model to disk in the 'models' folder
    dump(rf_model, 'models/rf_model.joblib')
     # Return model, predictions, and evaluation metrics
    return rf_model, y_pred, metrics

# Function to load an existing model if it exists, otherwise train a new one
def load_or_train_model(data):
    # If the model is already saved, load and return it
    if os.path.exists('models/rf_model.joblib'):
        return load('models/rf_model.joblib')
    
     # If model doesn't exist, train and return it
    rf_model, _, _ = train_random_forest(data)
    return rf_model
