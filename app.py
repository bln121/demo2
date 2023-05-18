import streamlit as st
import pandas as pd
import urllib.request

def main():
    st.title("Display Image in Streamlit DataFrame")
    
    # Create a DataFrame
    df = pd.DataFrame(
         'https://raw.githubusercontent.com/bln121/demo2/main/correct.png',columns=['Image']
        
    )
    
    # Retrieve the image from the GitHub repository
    df['Image'] = df['Image'].apply(lambda url: Image.open(urllib.request.urlopen(url)))
    
    # Display the DataFrame with the image
    st.dataframe(df)

if __name__ == '__main__':
    main()
