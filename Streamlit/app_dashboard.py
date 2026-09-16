import streamlit as st

st.title("Simple Sales Dashboard")
months = st.sidebar.selectbox('Select Month', ['January', 'February', 'March', 'April'])

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

st.metric(label=f"Sales for {months}", value=f"₹{sales[months]}")

st.bar_chart(list(sales.values()), x_label='Month', y_label='Sales')