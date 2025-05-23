from .helpers import get_bmi_category

def get_recommendations(data, rf_model, bmi, goal, meal_preference, y_pred, num_recommendations=5):
    filtered_data = data[data['meal_type'] == meal_preference.lower()].copy()
    filtered_data['is_high_calorie'] = (y_pred[filtered_data.index] == 1)
    bmi_category = get_bmi_category(bmi)
    
    # Use meal-type specific mean calories instead of global mean
    mean_cal = filtered_data['calories'].mean()

    if goal == "Weight Loss":
        if bmi <= 18.5:
            return [{"name": "❌ You're underweight for weight loss. Please consult a doctor."}]
        else:
            filtered_data = filtered_data[filtered_data['calories'] < mean_cal]
            filtered_data = filtered_data.sort_values(by=['calories', 'protein'], ascending=[True, False])

    elif goal == "Weight Gain":
        if bmi >= 25:
            return [{"name": "❌ Your BMI is too high for weight gain. Please consider Healthy Living."}]
        else:
            filtered_data = filtered_data[filtered_data['calories'] > mean_cal]
            filtered_data = filtered_data.sort_values(by=['calories', 'protein'], ascending=[False, False])

    elif goal == "Healthy Living":
        if bmi < 18.5 or bmi > 24.9:
            return [{"name": "❌ Your BMI is not in the normal range. Please choose Weight Loss or Gain instead."}]
        else:
            filtered_data['calorie_diff'] = abs(filtered_data['calories'] - 250)
            filtered_data = filtered_data.sort_values(by=['calorie_diff', 'protein'], ascending=[True, False])

    # Fallback if no results after filtering
    if filtered_data.empty:
        filtered_data = data[data['meal_type'] == meal_preference.lower()]
        filtered_data = filtered_data.sort_values(by=['calories', 'protein'], ascending=[False, False])

    return filtered_data.head(num_recommendations)[['name', 'calories', 'protein']].to_dict('records')
