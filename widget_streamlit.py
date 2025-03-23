import streamlit as st
import numpy as np
import pandas as pd


st.title("Streamlit Text Input")

name = st.text_input("Enter your name",)

age = st.slider("Enter your age", 0, 100, 25)

st.write(f"Your age is {age}")

option = ["Python", "Java", "C++", "JavaScript"]
lang = st.selectbox("Select your favorite programming language", option)
st.write(f"Your favorite programming language is {lang}")

if name:
    st.write(f"Hello {name}")
    
Data = {
    "Name": ["Tom", "Jerry", "Mickey", "Donald"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "California", "Florida", "Texas"]
}

df = pd.DataFrame(Data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)