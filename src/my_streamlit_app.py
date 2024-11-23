import streamlit as st
import numpy as np
import pandas as pd

st.write("Hello World!")

# This array is recreated with each page interaction
array = np.random.randn(5, 10)
cols = array.shape[1]

st.write("Write array as interactive dataframe...")
st.dataframe(array)

st.write("Write as static table...")
st.table(array)

st.write("With Pandas Styler, highlighting max per column...")
df = pd.DataFrame(
    array,
    columns=('col %d' % i for i in range(cols)))

st.dataframe(df.style.highlight_max(axis=0))

st.write("Write array as static table...")
st.table(df)

if st.checkbox('Show chart'):
    st.line_chart(df)

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

# Every widget with a key is automatically added to Session State.
st.text_input("Your name", key="name")
st.write(st.session_state.name)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

st.sidebar.write("You selected: ", add_selectbox)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)