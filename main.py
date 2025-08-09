import streamlit as st
import json
import os
from predict_page import show_prediction_page

# Load users from JSON
def load_users():
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            return json.load(f)
    return {}

# Save new user
def save_user(username, password):
    users = load_users()
    users[username] = password
    with open("users.json", "w") as f:
        json.dump(users, f)

# Login form
def login_page():
    st.title("🔐 Login to House Price Estimator")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login = st.button("Login")
    
    if login:
        users = load_users()
        if username in users and users[username] == password:
            st.success("Login successful!")
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
        else:
            st.error("Invalid credentials")

# Signup form
def signup_page():
    st.title("📝 Create a New Account")
    username = st.text_input("Choose a username")
    password = st.text_input("Choose a password", type="password")
    signup = st.button("Sign Up")
    
    if signup:
        users = load_users()
        if username in users:
            st.warning("Username already exists.")
        else:
            save_user(username, password)
            st.success("Account created! You can now log in.")

# Navigation
def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    st.sidebar.title("Navigation")
    option = st.sidebar.radio("Select", ["Login", "Signup"])

    if st.session_state['logged_in']:
        show_prediction_page()
    elif option == "Login":
        login_page()
    else:
        signup_page()

if __name__ == "__main__":
    main()
