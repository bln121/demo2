import pandas as pd
from PIL import Image
import requests
from io import BytesIO
import streamlit as st

# Fetch the image from Google
image_url = "https://tse4.mm.bing.net/th?id=OIP.B6TRJxR2eA7DYGmNyaYG3AHaJX&pid=Api&P=0&h=180"
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))


# Create the dataframe
data = {'Image': [image]}
df = pd.DataFrame(data)

st.write(df)
