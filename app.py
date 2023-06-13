import streamlit as st
import pandas as pd
import gspread

# URL of the Google Sheets document
sheet_url = 'https://docs.google.com/spreadsheets/d/1jJH8_IAVNIJdNsHAdDLy3DaebK8nb_Vy9ca5I7A2CfY/edit?usp=sharing'

# Read the Google Sheets document into a Pandas DataFrame
df_list = pd.read_html(sheet_url)

# Select the appropriate DataFrame from the list
df = df_list[0]  # Change the index if needed

# Display the DataFrame in Streamlit
st.write(df)

# Get user input for signup data
name = st.text_input("Enter your name:")
email = st.text_input("Enter your email:")
phone = st.text_input("Enter your phone number:")

# Create a new row with the signup data
new_row = [name, email, phone]

# Append the new row to the existing DataFrame
df = df.append(pd.Series(new_row, index=df.columns), ignore_index=True)

# Update the Google Sheets document
gc = gspread.models.Spreadsheet()
gc.id = sheet_url.split("/")[5]
worksheet = gc.get_worksheet(0)  # Assuming data is on the first worksheet
worksheet.append_row(new_row)

# Display the updated DataFrame
st.write(df)
