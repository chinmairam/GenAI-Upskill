import streamlit as st
import pandas as pd

st.write("Hello World")
st.title("Hello Streamlit")
st.write("This is my first streamlit app")
st.header("Welcome to Streamlit")
st.subheader("This is a subheader")
st.text("This is plain text")

## Button, Checkbox, Slider
if st.button("Click me!"):
    st.write("Button clicked")

agree = st.checkbox("I agree!")
if agree:
    st.write("You agreed!")

level = st.slider("Select a Level: ", 1, 10, 5)
st.write(f"Selected Level: {level}")

uploaded_file = st.fileuploader("Upload a File", type=["csv", "txt"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())