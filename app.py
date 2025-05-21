import streamlit as st
from modules.data_utils import load_and_prepare_data
from modules.model_utils import load_or_train_model
from modules.ui_components import home_page, user_input_page

# Must be first Streamlit command
st.set_page_config(page_title="Nutrition Recommender", layout="wide")

def main():
    if 'page' not in st.session_state:
        st.session_state.page = "home"

    st.session_state.data = load_and_prepare_data()
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
    
if __name__ == "__main__":
    main()
