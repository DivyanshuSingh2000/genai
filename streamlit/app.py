import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Simple Streamlit App")

# Display a simple text
st.write("Hello, welcome to the Streamlit app!")

# Create a sample DataFrame
data = { 'Column 1': np.random.rand(10), 'Column 2': np.random.rand(10) }
df = pd.DataFrame(data)

st.write("Here is a sample DataFrame:")
st.dataframe(df)

# create a simple line chart
st.line_chart(df)