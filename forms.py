import streamlit as st 
import pandas as pd
import numpy as np

def get_data():
    df = pd.DataFrame({
        "lat":np.random.randn(200)/50 +37.76,
        "lon":np.random.randn(200)/50 + -122.4,
        "team":["A","B"] * 100
    })
    return df

# st.dataframe(get_data())
if st.button("Generate new points"):
    st.session_state.df = get_data()

if 'df' not in st.session_state:
    st.session_state.df = get_data()

df = st.session_state.df

with st.form("my_form"):
    header = st.columns([1,2,2])
    header[0].subheader('Color')
    header[1].subheader('Opacity')
    header[2].subheader('Size')

    row1 = st.columns([1,2,2])
    colorA = row1[0].color_picker('Team A', '#0000FF')
    opacityA = row1[1].slider('A Opacity',20,100,50, label_visibility="hidden")
    sizeA = row1[2].slider("A Size",50,200,100, step=10, label_visibility="hidden")

    row2 = st.columns([1,2,2])
    colorB = row2[0].color_picker('Team B', '#FF0000')
    opacityB = row2[1].slider('B Opacity',20,100,50, label_visibility="hidden")
    sizeB = row2[2].slider("B Size",50,200,100, step=10, label_visibility="hidden")

    st.form_submit_button("Update Map")

alphaA = int(opacityA*255/100)
alphaB = int(opacityB*255/100)

df['color'] = np.where(df.team == 'A', colorA+f"{alphaA:02x}",colorB+f"{alphaB:02x}")
df["size"] = np.where(df.team == 'B', sizeA,sizeB)

st.map(df,size='size', color='color')

# st.dataframe(df)

# Widget values
st.title("Widget values")
# Before a form is submitted, all widgets within that form will have default values, just like widgets outside of a form have default values.

with st.form("form1"):
    st.write("Inside the form")
    my_number = st.slider("Pick a number", 1,10)
    my_color = st.selectbox("Pick a color",['red','orange','green','blue','violet'])

    st.form_submit_button("Submit my picks")

# This is outside the form
st.write(my_number)
st.write(my_color)