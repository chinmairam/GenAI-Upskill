import streamlit as st

price = st.number_input("Enter Product Price")
discount_percent = st.slider(
    label="Select Discount %",
    min_value=0,
    max_value=50,
    format="%d%%"
)
st.write(f"You selected: {discount_percent}%")

calc_price = st.button("Calculate Discounted Price")

if calc_price:
    final_price = price-(price*discount_percent/100)
    st.success(f"Price Calcualted successfully: ₹{final_price}", icon="✅")
    st.table([
        ["", "Price"],
        ["Before", f"₹{price}"],
        ["After", f"₹{final_price}"],
    ])
