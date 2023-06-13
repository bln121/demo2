import streamlit as st
import pandas as pd
import gspread

# Open the Google Sheets document
sheet = gspread.open_by_url('https://docs.google.com/spreadsheets/d/your-sheet-id/edit#gid=your-sheet-gid')

# Get the first sheet of the document
worksheet = sheet.get_worksheet(0)

# Get all values from the worksheet
data = worksheet.get_all_values()

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame in Streamlit
st.write(df)
