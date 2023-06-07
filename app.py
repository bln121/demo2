import streamlit as st
import base64
import requests

GITHUB_TOKEN = "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"
GITHUB_REPO = "bln121/demo2"
FILE_PATH = "credentials.txt"

def update_file(username, password):
    file_contents = f"{username}:{password}\n"

    # Encode file contents to base64
    file_contents_encoded = base64.b64encode(file_contents.encode()).decode()

    # Build the API URL
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{FILE_PATH}"

    # Create the headers with the Authorization token
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Get the current file content
    response = requests.get(url, headers=headers)
    response_json = response.json()

    if "content" in response_json:
        # Update the file content
        sha = response_json["sha"]
        data = {
            "message": "Update user credentials",
            "content": file_contents_encoded,
            "sha": sha
        }
        response = requests.put(url, headers=headers, json=data)
    else:
        # Create a new file
        data = {
            "message": "Create user credentials",
            "content": file_contents_encoded
        }
        response = requests.put(url, headers=headers, json=data)

    if response.status_code == 201 or response.status_code == 200:
        st.success("Signup successful! Please proceed to login.")
    else:
        st.error("Failed to update the file. Please try again.")

def signup_page():
    st.header("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        update_file(username, password)

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
    #login_page()
else:
    st.title("Dashboard")
    st.write("This is the authenticated area of the app.")
    # Add your main application code here
