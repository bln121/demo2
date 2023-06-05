import streamlit as st
import bcrypt  # for password hashing

def save_credentials(username, password):
    with open("C:\Users\raman\OneDrive\Desktop\credentials.txt", "a") as file:
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        file.write(f"{username}:{hashed_password.decode('utf-8')}\n")
        st.success("Signup successful! Please proceed to login.")

def check_credentials(username, password):
    with open("user_credentials.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username:
                if bcrypt.checkpw(password.encode("utf-8"), stored_password.encode("utf-8")):
                    st.success("Login successful!")
                    return True
                else:
                    st.error("Incorrect password. Please try again.")
                    return False
        st.error("User not found. Please sign up first.")
        return False

def signup_page():
    st.header("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        save_credentials(username, password)

def login_page():
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        check_credentials(username, password)

session_state = st.session_state

if not session_state.get("logged_in"):
    st.title("Welcome to My App")
    signup_page()
    login_page()
else:
    st.title("Dashboard")
    st.write("This is the authenticated area of the app.")
    # Add your main application code here
