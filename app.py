import streamlit as st
import pandas as pd

# URL of the Google Sheets document
sheet_url = 'https://docs.google.com/spreadsheets/d/1jJH8_IAVNIJdNsHAdDLy3DaebK8nb_Vy9ca5I7A2CfY/edit?usp=sharing'

# Read the Google Sheets document into a Pandas DataFrame
df_list = pd.read_html(sheet_url)

# Select the appropriate DataFrame from the list
df = df_list[0]  # Change the index if needed

# Display the DataFrame in Streamlit
st.write(df)
