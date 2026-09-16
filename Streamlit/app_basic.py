import streamlit as st

st.title("Welcome to Streamlit!")

user_name = st.text_input(
    label="Enter your name",
    value="",
    placeholder="Type here..."
)

greet = st.button("Greet Me")
if greet:
    st.write(f"Hello, {user_name}!")