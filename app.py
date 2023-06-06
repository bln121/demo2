import json
import os

CREDENTIALS_FILE = "user_credentials.json"

def save_credentials(username, password):
    user_credentials = load_credentials()
    user_credentials[username] = password
    save_to_file(user_credentials)
    st.success("Signup successful! Please proceed to login.")

def check_credentials(username, password):
    user_credentials = load_credentials()
    if username in user_credentials:
        if user_credentials[username] == password:
            st.success("Login successful!")
            return True
        else:
            st.error("Incorrect password. Please try again.")
            return False
    else:
        st.error("User not found. Please sign up first.")
        return False

def load_credentials():
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "r") as file:
            return json.load(file)
    else:
        return {}

def save_to_file(user_credentials):
    with open(CREDENTIALS_FILE, "w") as file:
        json.dump(user_credentials, file)

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
