import pandas as pd
import streamlit as st

# title of the application
st.title("Streamlit Text Input")

name = st.text_input("Enter your name")
age = st.slider("Select your age", 0, 100, 25)

if name:
    st.write(f"Hello {name}, you are {age} years old!")

options = ["Python", "Java", "C++", "JavaScript", "Go", "Ruby"]
selectedLanguage = st.selectbox("Select your favorite programming language", options)
st.write(f"You selected: {selectedLanguage}")

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
df.to_csv('data.csv')

st.write("Here is a sample dataframe:")
st.dataframe(df)

uploadedFile = st.file_uploader("Upload a CSV file", type=["csv"])
if uploadedFile is not None:
    df = pd.read_csv(uploadedFile)
    st.write(df)
