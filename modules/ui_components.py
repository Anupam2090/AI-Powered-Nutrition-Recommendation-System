import streamlit as st
from .helpers import get_bmi_category
from .model_utils import train_random_forest
from .recommend_utils import get_recommendations

# ------------------- HOME PAGE FUNCTION -------------------
def home_page():
    st.title("🥗 Nutrition Recommendation System")
    st.write("Select your goal to get started:")
    goals = {
        "Weight Loss": "🏋️‍♀️ Lose weight healthily.",
        "Weight Gain": "💪 Gain weight effectively.",
        "Healthy Living": "🥗 Maintain a healthy lifestyle."
    }
     # Show each goal as a subheader and clickable button
    for goal, desc in goals.items():
        st.subheader(goal)
        st.markdown(f"<p>{desc}</p>", unsafe_allow_html=True)
          # If user clicks the button for this goal:
        if st.button(goal):
             # Save the chosen goal as the current page in session
            st.session_state.page = goal.lower().replace(" ", "_")
              # Refresh the app to switch to the input page
            st.rerun()
            
# ------------------- USER INPUT PAGE FUNCTION -------------------
def user_input_page(goal):
    # Show the goal-specific title
    st.title(f"{goal} Recommendation")

    try:
         # Input fields for user data
        age = st.number_input("Age", 0, 100, 25)
        weight = st.number_input("Weight (kg)", 0.0, 200.0, 70.0)
        height = st.number_input("Height (m)", 0.1, 2.5, 1.75)
        meal_preference = st.selectbox("Meal Type", ["Breakfast", "Lunch", "Dinner"])

         # Calculate BMI = weight (kg) / height^2 (m^2)
        bmi = weight / (height ** 2)
        bmi_category = get_bmi_category(bmi)
         # Display the BMI and category
        st.write(f"Your BMI: {bmi:.2f} ({bmi_category})")
        
    #  When user clicks the "Get Recommendations" button:
        if st.button("Get Recommendations"):
            st.info("Generating recommendations...")
            
             # Train the Random Forest model using the loaded data
            rf_model, y_pred, _ = train_random_forest(st.session_state.data)
            # Get recommendations based on input
            recs = get_recommendations(
                st.session_state.data,  # full dataset
                rf_model,                # trained model
                bmi,        # user's BMI
                goal,       # selected goal
                meal_preference,    ## breakfast/lunch/dinner
                y_pred               # prediction from model
            )

             # Display the top recommendations
            st.subheader("Recommended Foods")
            for i, food in enumerate(recs):
                st.markdown(f"**{i+1}. {food['name']}**")
                st.markdown(f"- Calories: {food['calories']} kcal\n- Protein: {food['protein']} g")
     # Catch any runtime errors and show them
    except Exception as e:
        st.error(f"⚠️ An error occurred: {e}")

# ✅ Add Return to Home
    if st.button("🏠 Return to Home"):
        st.session_state.page = "home"
        st.rerun()  # Refresh the app