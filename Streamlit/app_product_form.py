import streamlit as st

product_name = st.sidebar.text_input("Enter product name:")
category = st.sidebar.selectbox("Choose a Category:", ["Electronics", "Home Decor", "Kitchenware"])
price = st.sidebar.number_input("Enter Price:")

add_product = st.button("Add Product")
if add_product:
    st.success("Product added successfully")
    st.table([
        ["Product", "Category", "Price"],
        [f"{product_name}", f"{category}", f"{price}"]
    ])