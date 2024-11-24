import streamlit as st
import numpy as np
import pandas as pd
import time

st.write("Hello World!")

# Reload the page
if st.button("Reload"):
    st.rerun()

if "reload_count" not in st.session_state:
    st.session_state.reload_count = 0
else:
    st.session_state.reload_count += 1
    
st.write(f"We've reloaded {st.session_state.reload_count} times")
    
# This array WOULD BE recreated with each page interaction
# So let's store it in a session variable
if "rand_array" not in st.session_state:
    st.session_state.rand_array = np.random.randn(5, 10)

cols = st.session_state.rand_array.shape[1]

df = pd.DataFrame(
    st.session_state.rand_array,
    columns=('c %d' % i for i in range(cols)))

st.line_chart(df.T, x_label="Col")
  
with st.expander("Expand tables...", expanded=False):  
    st.write("Write array using magic command...")
    st.session_state.rand_array # print using magic command - an alias for st.write()
        
    # Create two cols
    left_column, right_column = st.columns(2)

    left_column.write("Write array as interactive dataframe...")
    left_column.dataframe(st.session_state.rand_array)

    right_column.write("With as DF with Pandas Styler, highlighting max...")
    right_column.dataframe(df.style.highlight_max(axis=0))
    
    st.write("Write array as static table...")
    st.table(df)

### Use st.sidebar to place in left sidebar ###
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

st.sidebar.write("You selected: ", add_slider)

linear_df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })
linear_df['index'] = linear_df.index # Create new column for x axis

x = np.arange(-10, 11, 1)  # Creates a NumPy array from -10 to 10
y = x**2
quadratic_df = pd.DataFrame({'x': x, 'y': y}) 

# This expander will only show if we've checked a chart in the menu
with st.expander("Expand charts", expanded=True):  
    if st.sidebar.checkbox('Show linear chart on main panel'):
        # Let's put the chart in the main panel
        st.line_chart(linear_df, x='index', y=['first column', 'second column'])
        # st.sidebar.line_chart(linear_df)

    if st.sidebar.checkbox('Show quadratic chart on main panel', value=True):
        st.line_chart(quadratic_df['y'], x_label="x", y_label="y")

chosen = st.sidebar.radio(
    'Sorting hat',
    ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"), index=3)
st.sidebar.write(f"You are in {chosen} house!")
    
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

# Every widget with a key is automatically added to Session State.
st.text_input("Your name", key="name")
st.write(st.session_state.name)

if st.button('Start long process'):
    "Starting a long computation..."

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.02)

    """...and now we're done!"""


