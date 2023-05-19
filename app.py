import pandas as pd
import streamlit as st

# Create a DataFrame
data = {
    'Name': ['John', 'Jane', 'Adam'],
    'Age': [25, 30, 35],
    'Image': ['https://tse4.mm.bing.net/th?id=OIP.B6TRJxR2eA7DYGmNyaYG3AHaJX&pid=Api&P=0&h=180', '', '']
}
df = pd.DataFrame(data)

# Iterate over the DataFrame and display the images
for index, row in df.iterrows():
    image_path = row['Image']
    st.write(f"Name: {row['Name']}")
    st.write(f"Age: {row['Age']}")
    st.image(image_path, caption=row['Name'], use_column_width=True)
