import streamlit as st
import openai

openai.api_key = st.secrets["openai"]["sk-...GSUA"]

st.title("🌱 AI Eco Product Scanner")
st.write("Type a product name and get its environmental impact!")

product = st.text_input("Enter a product name:")

if st.button("Analyze"):
    if product:
        prompt = f"""
        Analyze the environmental impact of this product: {product}.
        Give:
        1. Material type
        2. Recyclability
        3. Environmental impact
        4. Eco-friendly suggestion
        """

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            result = response['choices'][0]['message']['content']
            st.success("AI Analysis:")
            st.write(result)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a product name.")
