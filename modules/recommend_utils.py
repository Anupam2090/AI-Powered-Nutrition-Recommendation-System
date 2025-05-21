from .helpers import get_bmi_category

def get_recommendations(data, rf_model, bmi, goal, meal_preference, y_pred, num_recommendations=5):
    filtered_data = data[data['meal_type'] == meal_preference.lower()].copy()
    filtered_data['is_high_calorie'] = (y_pred[filtered_data.index] == 1)
    bmi_category = get_bmi_category(bmi)
    mean_cal = data['calories'].mean()

    # Apply filters based on BMI and goal
    if bmi_category == "Underweight" and goal != "Weight Loss":
        filtered_data = filtered_data[filtered_data['calories'] > mean_cal]
    elif bmi_category in ["Normal", "Overweight", "Obese"] and goal == "Weight Loss":
        filtered_data = filtered_data[filtered_data['calories'] < mean_cal]

    sorted_data = filtered_data.sort_values('calories', ascending=False)
    return sorted_data.head(num_recommendations).to_dict('records')
