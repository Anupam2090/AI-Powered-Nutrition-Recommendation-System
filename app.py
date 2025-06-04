# Import required modules
import streamlit as st
from modules.data_utils import load_and_prepare_data
from modules.model_utils import load_or_train_model
from modules.ui_components import home_page, user_input_page
from db.db_utils import delete_user

# Import database utility functions
from db.db_utils import login_user, register_user

# Streamlit App Setup
st.set_page_config(page_title="Nutrition Recommender", layout="wide")

# --------------------------
# Login/Register Components
# --------------------------
def show_login():
    st.subheader("🔐 Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = login_user(email, password)
        if user:
            st.success("Login successful!")
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.session_state.page = "home"  # 👈 Go to home or weight_loss etc.
            st.rerun()
        else:
            st.error("Invalid credentials.")
    if st.button("Go to Register"):
        st.session_state.page = "register"
        st.rerun()


def show_register():
    st.subheader("📝 Register")
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        if register_user(name, email, password):
            st.success("✅ Registration successful! Please login.")
            st.session_state.page = "login"
            st.rerun()
        else:
            st.error("❌ Registration failed. User might already exist.")
    if st.button("Go to Login"):
        st.session_state.page = "login"
        st.rerun()

# --------------------------
# Main App Logic
# --------------------------
def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'page' not in st.session_state:
        st.session_state.page = "login"

    if not st.session_state.logged_in:
        if st.session_state.page == "register":
            show_register()
        else:
            show_login()
    else:
        # Load model/data only once after login
        if 'data' not in st.session_state:
            st.session_state.data = load_and_prepare_data()
            st.session_state.rf_model = load_or_train_model(st.session_state.data)

        # Logout button
        with st.container():
            col1, col2 = st.columns([10, 1])
            with col2:
                if st.button("🔒 Logout"):
                    if 'user_email' in st.session_state:
                        # Delete user from DB
                        if delete_user(st.session_state.user_email):
                            st.success("User deleted successfully on logout.")
                        else:
                            st.error("Failed to delete user on logout.")
                    st.session_state.clear()
                    st.session_state.page = "login"
                    st.rerun()

        # Page routing
        if st.session_state.page == "home":
            home_page()
        elif st.session_state.page == "weight_loss":
            user_input_page("Weight Loss")
        elif st.session_state.page == "weight_gain":
            user_input_page("Weight Gain")
        elif st.session_state.page == "healthy_living":
            user_input_page("Healthy Living")
        


# Run the app
if __name__ == "__main__":
    main()
