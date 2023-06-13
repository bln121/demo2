import streamlit as st
import pandas as pd
import gspread

# Open the Google Sheets document
gc = gspread.service_account()
sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1jJH8_IAVNIJdNsHAdDLy3DaebK8nb_Vy9ca5I7A2CfY/edit?usp=sharing')

# Get the first sheet of the document
worksheet = sheet.get_worksheet(0)

# Get all values from the worksheet
data = worksheet.get_all_values()

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame in Streamlit
st.write(df)
