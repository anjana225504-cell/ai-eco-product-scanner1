import streamlit as st

st.title("🌱 AI Eco Product Scanner")
st.write("Type a product name and get its environmental impact!")

product = st.text_input("Enter a product name:")

if st.button("Analyze"):
    if product:
        st.success(f"Analyzing: {product}")
        st.write("Material: Plastic (example)")
        st.write("Recyclable: Yes (example)")
        st.write("Suggestion: Use reusable alternatives (example)")
