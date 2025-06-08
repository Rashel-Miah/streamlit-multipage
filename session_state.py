import streamlit as st 
import datetime

# Example 1: Add Session State
st.title("Counter Example")
if 'count' not in st.session_state:
    st.session_state['count'] = 0

increment = st.button("Increment", key="btn1")

if increment:
    st.session_state.count += 1

st.write('Count = ', st.session_state.count)

# Example 2: Session State and Callbacks

st.title("Counter example using Callbacks")
if 'count2' not in st.session_state:
    st.session_state.count2 = 0

def increment_counter2():
    st.session_state['count2'] += 1

st.button("Increment", on_click=increment_counter2, key="btn2")
st.write(st.session_state.count2)

# Example 3: Use args and kwargs in Callbacks
st.title("Counter Example using Callbacks with args and kwargs")
if 'count3' not in st.session_state:
    st.session_state.count3 = 0

increment_value3 = st.number_input("Enter a value", value=0, step=1)

def increment_counter3(increment_value3):
    st.session_state.count3 += increment_value3

def decrement_counter3(decrement_value3=0):
    st.session_state.count3 -= decrement_value3

btn3, btn3_1 = st.columns(2) # Placing these two buttons side by side
increment3 = btn3.button("Increment", on_click=increment_counter3,args=(increment_value3,), key="btn3") # args: example
decrement3 = btn3_1.button("Decrement", on_click=decrement_counter3,kwargs=dict(decrement_value3 = 1), key="btn3_1") #kwargs: example

st.write("Count = ", st.session_state.count3)

# Example 4: Forms and Callbacks
st.title("Counter Example using Forms and Callbacks")

if 'count4' not in st.session_state:
    st.session_state.count4 = 0
    st.session_state.last_updated = datetime.time(0,0)

def update_counter():
    st.session_state.count4 += st.session_state.increment_value
    st.session_state.last_updated = st.session_state.update_time

with st.form(key="my_form"):
    st.time_input(label="Enter the time", value=datetime.datetime.now().time(),key="update_time")
    st.number_input("Enter a value", value=0, step=1, key="increment_value")
    submit = st.form_submit_button(label="Update", on_click=update_counter)

st.write("Current Count = ", st.session_state.count4)
st.write("Last Updated = ", st.session_state.last_updated)

# Session State and Widget State association
# Here, Session State variables mirror the widget value using the key argument.
st.title("Example of Session State and Widget State association")

if "celsius" not in st.session_state:
    st.session_state['celsius'] = 50.0

st.slider(
    "Temperature in Celsius", 
    min_value=10.0, 
    max_value=100.0, 
    key="celsius") # It will mirror the session state 'celsius' varaible
# This will get the value of the slider widget
st.write(st.session_state.celsius)

# Finally see the all session variables
st.title("See all the session variables")
st.session_state