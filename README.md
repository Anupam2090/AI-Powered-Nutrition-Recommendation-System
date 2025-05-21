# Nutrition Recommendation System

🥗 A Streamlit-based interactive application that provides personalized nutrition recommendations based on user goals such as weight loss, weight gain, and healthy living.

---

## Features

- User-friendly interface for selecting goals and entering personal data.
- Calculates BMI and categorizes it for better insight.
- Uses a trained Random Forest model to generate food recommendations.
- Allows users to select meal preferences (Breakfast, Lunch, Dinner).
- Easy navigation with the option to return to the home page.
- Modular design with separate files for data processing, modeling, and UI components.

---

# Project File Overview

nutrition-recommender/
│
├── app.py # Main Streamlit app entry point
├── data/
│ └── nutrition.xlsx # Dataset file containing nutrition data
├── models/
│ └── rf_model.joblib # Saved Random Forest model file
├── modules/
│ ├── init.py # Makes modules a Python package
│ ├── data_utils.py # Functions for data loading and preprocessing
│ ├── model_utils.py # Functions for model training and prediction
│ ├── recommend_utils.py # Logic for generating food recommendations
│ ├── ui_components.py # Streamlit UI components and page layouts
│ └── helpers.py # Helper functions (e.g., BMI calculation, categories)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/nutrition-recommender.git
   cd nutrition-recommender

2. Create and activate a virtual environment (optional but recommended):

    ```
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate

    ```
3. Install required packages:
     ```
    pip install -r requirements.txt
     ```
4. Run the Streamlit app:

    ```
    streamlit run main.py
    
    ```
    Start on the home page and select your nutrition goal.

    Enter your personal data (age, weight, height, meal preference).

    Get customized nutrition recommendations.

    Use the "Return to Home" button to go back to the main menu.

## How It Works

    The app loads and prepares the nutrition dataset.

    It trains or loads a pre-trained Random Forest model to predict suitable foods.

    Based on user input and BMI, it generates and displays personalized food recommendations.

    Streamlit handles page navigation using st.session_state for smooth UX.

## Contact

    For questions or feedback, reach out at anupam06122001@gmail.com.


