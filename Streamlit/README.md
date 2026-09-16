# Streamlit Practice Apps

A collection of beginner Streamlit apps built as part of the GenAI Module 6 learning exercises.

## Apps

| File | Description |
|------|-------------|
| [app_basic.py](app_basic.py) | Text input and greet button — basic widget interaction |
| [app_discount.py](app_discount.py) | Discount calculator — number input, slider, and Before/After price comparison table |
| [app_dashboard.py](app_dashboard.py) | Sales dashboard — sidebar month selector, `st.metric()` KPI card, and bar chart |
| [app_product_form.py](app_product_form.py) | Product form — sidebar inputs (name, category, price) with a summary table on submit |

## Running an App

```bash
streamlit run app_basic.py
```

Replace `app_basic.py` with any filename above.

## Concepts Covered

- Text elements: `st.title`, `st.write`
- Input widgets: `st.text_input`, `st.number_input`, `st.slider`, `st.selectbox`, `st.button`
- Sidebar: `st.sidebar`
- Output: `st.success`, `st.metric`, `st.table`, `st.bar_chart`