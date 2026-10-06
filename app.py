import streamlit as st

st.title("AI-Based Product Price Verification System")

st.write("Enter product details to verify the price.")

product_name = st.text_input("Product Name")
mrp = st.number_input("MRP (₹)", min_value=0.0)
listed_price = st.number_input("Listed Price (₹)", min_value=0.0)
reference_price = st.number_input("Reference Price (₹)", min_value=0.0)
seller = st.text_input("Seller / Website")

if st.button("Verify Price"):
    if listed_price <= reference_price:
        st.success("Price Verified")
    else:
        difference = listed_price - reference_price
        st.warning(f"Price Mismatch — Difference: ₹{difference:.2f}")
