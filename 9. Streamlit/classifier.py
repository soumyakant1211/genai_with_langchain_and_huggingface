import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    return df, iris.target_names

df, target_names = load_data()

st.title("Iris Flower Classifier")
st.write("This application classifies iris flowers based on their features.")

model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['target'])
st.write("Model trained on the Iris dataset.")

sepalLength = st.slider("Sepal Length (cm)", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
sepalWidth = st.slider("Sepal Width (cm)", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
petalLength = st.slider("Petal Length (cm)", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petalWidth = st.slider("Petal Width (cm)", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

inputData = [[sepalLength, sepalWidth, petalLength, petalWidth]]

# Predict the class of the iris flower
prediction = model.predict(inputData)
st.write("Predicted class:", target_names[prediction[0]])