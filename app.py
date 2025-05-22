# Import Streamlit and rename it as 'st' for easier use
import streamlit as st
# Import custom function to load and clean the dataset
from modules.data_utils import load_and_prepare_data
# Import custom function to load or train a machine learning model
from modules.model_utils import load_or_train_model
# Import custom UI components for the home page and user input pages
from modules.ui_components import home_page, user_input_page

# Set up the configuration of the Streamlit web app
# page_title: title shown in browser tab
# layout="wide": makes full use of screen width
st.set_page_config(page_title="Nutrition Recommender", layout="wide")
# Define the main function to control app logic
def main():
    # If 'page' is not already in session_state, initialize it to "home"
    # This keeps track of which page the user is on
    if 'page' not in st.session_state:
        st.session_state.page = "home"
 # Load and prepare the data, then store it in session_state
    st.session_state.data = load_and_prepare_data()
     # Load an existing model or train a new one using the prepared data
    st.session_state.rf_model = load_or_train_model(st.session_state.data)

    if st.session_state.page == "home":
        home_page()
    elif st.session_state.page == "weight_loss":
        user_input_page("Weight Loss")
    elif st.session_state.page == "weight_gain":
        user_input_page("Weight Gain")
    elif st.session_state.page == "healthy_living":  
        user_input_page("Healthy Living")
    else:
        st.error("Unknown page!")
# This runs the main function when the script is executed directly 
if __name__ == "__main__":
    main()
