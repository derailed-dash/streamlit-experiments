import random
import streamlit as st
import numpy as np
import pandas as pd
import time

st.set_page_config(page_title="Experimenting with Streamlit", page_icon="📈")
st.sidebar.markdown("# Main page 🎈")

st.title("Experimenting with Streamlit")

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

@st.cache_data()
def quadratic_demo():
    x = np.arange(-10, 11, 1)  # Creates a NumPy array from -10 to 10
    y = x**2
    return pd.DataFrame({'x': x, 'y': y}) 

def generate_meow_data():
    if "meow_df" in st.session_state:
        return st.session_state.meow_df
    
    days = ['Monday', 'Tuesday', 'Wednesday']
    meow_data = {}

    for day in days:
        hourly_meows = []
        for hour in range(24):
            # Base meow rate
            meows = random.randint(1, 5)

            # Add peaks for dinner times (7:00 and 16:00)
            if hour in [7, 16]:
                meows += random.randint(10, 20)  # Increased meows around dinner
            elif hour in [6, 8, 15, 17]: # make it more realistic with tapering up and down
                meows += random.randint(5, 10)

            hourly_meows.append(meows)
        meow_data[day] = hourly_meows

    # Generate DF with dimensions of 5 cols and 24 rows
    meow_df = pd.DataFrame(meow_data)
    st.session_state.meow_df = meow_df
    return meow_df

def present_meow_data(df: pd.DataFrame):
    st.subheader("Meow Data") # Headings automatically get links
    with st.expander("Expand data and plots...", expanded=False):  
        # Create two cols
        left_column, right_column = st.columns(2)
    
        left_column.write("Write array as interactive dataframe...")
        left_column.dataframe(df)
    
        right_column.write("With DF with Pandas Styler, highlighting max...")
        right_column.dataframe(df.style.highlight_max(axis=0))
        
        st.write("Write static table...")
        st.table(df)
        
        st.bar_chart(df, x_label="Hour", y_label="Meows")
        st.line_chart(df, x_label="Hour", y_label="Meows")
        st.scatter_chart(df, x_label="Hour", y_label="Meows")
        
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
        
def advance_option():
    option_names = ["a", "b", "c"]

    radio_container = st.container() # create an invisible container
    next = st.button("Advance Option") # Now the button comes after the container

    if next:
        if st.session_state["radio_option"] == "a":
            st.session_state.radio_option = "b"
        elif st.session_state["radio_option"] == "b":
            st.session_state.radio_option = "c"
        elif st.session_state["radio_option"] == "c":
            st.session_state.radio_option = "a"

    option = radio_container.radio("Pick an option", option_names, key="radio_option")

def main():
    reload_counter()
    st.write("_Retrieve a secret:_ ", st.secrets["my_secret"])
    st.markdown("---") # Horizontal rule
    
    meow_df = generate_meow_data()
    present_meow_data(meow_df)
    
    st.subheader("Demonstrating Plotting", )
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
            st.markdown("#### Quadratic")
            st.line_chart(quadratic_df['y'], x_label="x", y_label="y")
        
        linear_chart_checkbox = st.sidebar.checkbox('Show linear chart on main panel')
        if linear_chart_checkbox:
            # Let's put the chart in the main panel
            st.markdown("#### Linear Plot")
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
    
    advance_option()
    
if __name__ == "__main__":
    main()
