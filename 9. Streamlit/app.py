import numpy as np
import pandas as pd
import streamlit as st

# title of the application
st.title("Hello World")

# display a text
st.write("This is a simple Streamlit application.")

# displaying a dataframe
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write("Here is a dataframe:")
st.write(df)

# displaying a line chart
st.write("Here is a line chart:")
chartData = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chartData)