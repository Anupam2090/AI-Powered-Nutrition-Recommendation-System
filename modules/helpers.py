# Function to determine BMI category based on the BMI value
def get_bmi_category(bmi):
    # If BMI is less than 18.5, person is underweight
    if bmi < 18.5:
        return "Underweight"
     # If BMI is between 18.5 (inclusive) and 25 (exclusive), person is normal weight
    elif 18.5 <= bmi < 25:
        return "Normal"
     # If BMI is between 25 (inclusive) and 30 (exclusive), person is overweight
    elif 25 <= bmi < 30:
        return "Overweight"
     # If BMI is 30 or higher, person is obese
    else:
        return "Obese"
