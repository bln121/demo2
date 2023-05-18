import streamlit as st
import pandas as pd
import urllib.request
from PIL import Image

def main():
    st.title("Display Image in Streamlit DataFrame")
    
    # Create a DataFrame
    df = pd.DataFrame({
        'Image': ['https://raw.githubusercontent.com/<USERNAME>/<REPO_NAME>/<BRANCH_NAME>/<PATH_TO_IMAGE>'],
        'Caption': ['Image Caption']
    })
    
    # Retrieve the image from the GitHub repository
    df['Image'] = df['Image'].apply(lambda url: Image.open(urllib.request.urlopen(url)))
    
    # Display the DataFrame with the image
    st.dataframe(df)

if __name__ == '__main__':
    main()
