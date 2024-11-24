import streamlit as st
import numpy as np
import pandas as pd
import time

st.sidebar.markdown("# Main page 🎈")

st.title("Experimenting with Streamlit")
st.write("---")

# Reload the page
if st.button("Reload"):
    st.rerun()

def reload_counter():
    # Store the counter in session state
    # Note that widgets many their own session state
    if "reload_count" not in st.session_state:
        st.session_state.reload_count = 0
    else:
        st.session_state.reload_count += 1
        
    st.write(f"We've reloaded {st.session_state.reload_count} times")

def present_array_data():
    st.subheader("Working with arrays and dataframes") # Headings automatically get links
    st.write(f"A random array of 5 rows and 10 columns, with normal distribution about 0.")
    # This array WOULD BE recreated with each page interaction
    # So let's store it in a session variable
    if "rand_array" not in st.session_state:
        # Use a normal distribution with mean of 0 and std dev of 1
        st.session_state.rand_array = np.random.randn(5, 10)

    col_labels = st.session_state.rand_array.shape[1]
    row_labels = [chr(ord('A') + i) 
                for i in range(st.session_state.rand_array.shape[0])] # Create labels 'A', 'B', 'C', etc.

    df = pd.DataFrame(
        st.session_state.rand_array,
        index=row_labels,
        columns=('c %d' % i for i in range(col_labels)))

    st.write(f"Plotted as a line chart...")
    st.line_chart(df.T, x_label="Col")

    with st.expander("Expand tables and plots...", expanded=False):  
        st.write("Write array using magic command...")
        st.session_state.rand_array # print using magic command - an alias for st.write()

        st.write(f"Plotted as a scatter chart, with data transposed...")
        st.scatter_chart(df, x_label="Col")        
        
        # Create two cols
        left_column, right_column = st.columns(2)

        left_column.write("Write array as interactive dataframe...")
        left_column.dataframe(st.session_state.rand_array)

        right_column.write("With as DF with Pandas Styler, highlighting max...")
        right_column.dataframe(df.style.highlight_max(axis=0))
        
        st.write("Write array as static table...")
        st.table(df)

@st.cache_data()
def quadratic_demo():
    x = np.arange(-10, 11, 1)  # Creates a NumPy array from -10 to 10
    y = x**2
    return pd.DataFrame({'x': x, 'y': y}) 

@st.cache_data()
def linear_plot_demo():
    linear_df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    })
    linear_df['index'] = linear_df.index # Create new column for x axis
    return linear_df

def demo_progress_bar():
    """ Demonstrate progress bar, as well as updating text in situ. """
    st.markdown("## Progress bars")
    progress_state = st.text('Not started')
    
    if st.button('Start long process'):
        progress_state.text("Starting a long computation...")

        # Add a placeholder
        latest_iteration = st.empty()
        bar = st.progress(0)

        for i in range(100):
            # Update the progress bar with each iteration.
            latest_iteration.text(f'Iteration {i+1}')
            bar.progress(i + 1)
            time.sleep(0.02)

        progress_state.text("...and now we're done!")

def main():
    reload_counter()
    st.write("_Retrieve a secret:_ ", st.secrets["my_secret"])
    st.markdown("---") # Horizontal rule
    present_array_data()

    quadratic_df = quadratic_demo()
    linear_df = linear_plot_demo()
    
    ######## Build Sidebar ########
    st.sidebar.subheader("Contact")    
    add_selectbox = st.sidebar.selectbox(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone')
    )
    st.sidebar.write("You selected: ", add_selectbox)

    # Add a slider to the sidebar
    st.sidebar.subheader("Range")   
    add_slider = st.sidebar.slider(
        'Select a range of values',
        0.0, 100.0, (25.0, 75.0)
    )
    st.sidebar.write("You selected: ", add_slider)
    
    st.sidebar.subheader("Charts")
    # This expander will only show if we've checked a chart in the menu
    with st.expander("Expand charts", expanded=True):
        quadratic_chart_checkbox = st.sidebar.checkbox('Show quadratic chart on main panel', value=True)
        if quadratic_chart_checkbox:
            st.subheader("Demonstrating a Quadratic")
            # Or we could use markdown, like this:
            # st.markdown("## Demonstrating a Quadratic")
            st.line_chart(quadratic_df['y'], x_label="x", y_label="y")
        
        linear_chart_checkbox = st.sidebar.checkbox('Show linear chart on main panel')
        if linear_chart_checkbox:
            # Let's put the chart in the main panel
            st.subheader("Demonstrating Linear Plot")
            st.line_chart(linear_df, x='index', y=['first column', 'second column'])
            # st.sidebar.line_chart(linear_df)

    st.sidebar.subheader("Sorting Hat")
    chosen = st.sidebar.radio(label="Sorting Hat", 
                              label_visibility="collapsed", # Hidden and collapsed
                              options=("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"), 
                              index=3)
    st.sidebar.write(f"You are in _{chosen}_ house!")
    ######## End Build Sidebar ########

    st.markdown("---")
    st.markdown("## Some Widgets")
    x_val = st.slider('Slider for Squares!')  # 👈 this is a widget
    st.write(x_val, 'squared is', x_val * x_val)

    # Every widget with a key is automatically added to Session State.
    st.text_input("Your name", key="name")
    st.write(st.session_state.name)

    st.markdown("---")
    demo_progress_bar()
    
if __name__ == "__main__":
    main()
