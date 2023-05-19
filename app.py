import streamlit as st
from PIL import Image

image = Image.open('https://tse4.mm.bing.net/th?id=OIP.B6TRJxR2eA7DYGmNyaYG3AHaJX&pid=Api&P=0&h=180')

st.image(image, caption='Sunrise by the mountains')
