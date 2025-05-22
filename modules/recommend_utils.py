# Import helper function to classify BMI
from .helpers import get_bmi_category

# Function to get recommended food items based on user's BMI, goal, and meal preference
def get_recommendations(data, rf_model, bmi, goal, meal_preference, y_pred, num_recommendations=5):
     # 1. Filter data for the selected meal type (e.g., 'breakfast', 'lunch', 'dinner')
    filtered_data = data[data['meal_type'] == meal_preference.lower()].copy()
    
     # 2. Add a new column to mark whether the food item is high calorie (based on model prediction)
    filtered_data['is_high_calorie'] = (y_pred[filtered_data.index] == 1)
    
     # 3. Get the BMI category (e.g., Underweight, Normal, Overweight, Obese)
    bmi_category = get_bmi_category(bmi)
    
     # 4. Calculate the mean calories from the whole dataset
    mean_cal = data['calories'].mean()

     # 5. Apply filtering logic based on BMI and user goal:
    # - If user is underweight and NOT trying to lose weight → recommend high calorie food
    if bmi_category == "Underweight" and goal != "Weight Loss":
        filtered_data = filtered_data[filtered_data['calories'] > mean_cal]
     # - If user is Normal/Overweight/Obese and trying to lose weight → recommend low calorie food
    elif bmi_category in ["Normal", "Overweight", "Obese"] and goal == "Weight Loss":
        filtered_data = filtered_data[filtered_data['calories'] < mean_cal]
        
     # 6. Sort the filtered data by calories in descending order (highest first)
    sorted_data = filtered_data.sort_values('calories', ascending=False)
     # 7. Return top N recommendations as a list of dictionaries
    return sorted_data.head(num_recommendations).to_dict('records')
