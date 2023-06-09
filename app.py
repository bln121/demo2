import streamlit as st
user_credentials = {}  # Initialize an empty dictionary

# Prompt the user to enter multiple usernames and passwords
while True:
    username = st.text_input("Username")
    if username == 'q':
        break
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        user_credentials[username] = password

# Display the stored use
st.write("Stored Usernames and Passwords:")
#for username, password in user_credentials.items():
    #print(f"Username: {username}, Password: {password}"
st.write(user_credentials)
