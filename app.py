import streamlit as st
import os

st.title("Welcome :smiley:")
st.header("I'm Laasya :smiley_cat:")
st.snow()

btn_click=st.button("Watchout")
if btn_click == True:
    st.header("You Got Me :stuck_out_tongue_winking_eye:")
    st.balloons()