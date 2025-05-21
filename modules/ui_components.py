import streamlit as st
from .helpers import get_bmi_category
from .model_utils import train_random_forest
from .recommend_utils import get_recommendations

def home_page():
    st.title("🥗 Nutrition Recommendation System")
    st.write("Select your goal to get started:")
    goals = {
        "Weight Loss": "🏋️‍♀️ Lose weight healthily.",
        "Weight Gain": "💪 Gain weight effectively.",
        "Healthy Living": "🥗 Maintain a healthy lifestyle."
    }
    for goal, desc in goals.items():
        st.subheader(goal)
        st.markdown(f"<p>{desc}</p>", unsafe_allow_html=True)
        if st.button(goal):
            st.session_state.page = goal.lower().replace(" ", "_")
            st.rerun()

def user_input_page(goal):
    st.title(f"{goal} Recommendation")

    try:
        age = st.number_input("Age", 0, 100, 25)
        weight = st.number_input("Weight (kg)", 0.0, 200.0, 70.0)
        height = st.number_input("Height (m)", 0.1, 2.5, 1.75)
        meal_preference = st.selectbox("Meal Type", ["Breakfast", "Lunch", "Dinner"])

        bmi = weight / (height ** 2)
        bmi_category = get_bmi_category(bmi)
        st.write(f"Your BMI: {bmi:.2f} ({bmi_category})")

        if st.button("Get Recommendations"):
            st.info("Generating recommendations...")

            rf_model, y_pred, _ = train_random_forest(st.session_state.data)
            recs = get_recommendations(
                st.session_state.data,
                rf_model,
                bmi,
                goal,
                meal_preference,
                y_pred
            )

            st.subheader("Recommended Foods")
            for i, food in enumerate(recs):
                st.markdown(f"**{i+1}. {food['name']}**")
                st.markdown(f"- Calories: {food['calories']} kcal\n- Protein: {food['protein']} g")

    except Exception as e:
        st.error(f"⚠️ An error occurred: {e}")

# ✅ Add Return to Home
    if st.button("🏠 Return to Home"):
        st.session_state.page = "home"
        st.rerun()