import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
products = [
    "plastic bottle",
    "plastic bag",
    "glass jar",
    "glass bottle",
    "paper cup",
    "paper bag",
    "steel bottle",
    "metal can"
]

materials = [
    "Plastic",
    "Plastic",
    "Glass",
    "Glass",
    "Paper",
    "Paper",
    "Metal",
    "Metal"
]

# AI training
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(products)

model = MultinomialNB()
model.fit(X, materials)

st.title("🌱 AI Eco Product Scanner")

product = st.text_input("Enter product name")

if st.button("Scan Product"):

    if product == "":
        st.write("Please enter a product name")

    else:
        test = vectorizer.transform([product])
        prediction = model.predict(test)[0]

        st.subheader("AI Sustainability Analysis")

        if prediction == "Plastic":
            st.write("Material:", prediction)
            st.write("Recyclable: Limited")
            st.write("Environmental Impact: High plastic pollution")
            st.write("Suggestion: Use reusable alternatives")
            st.write("Eco Score: Low")

        elif prediction == "Glass":
            st.write("Material:", prediction)
            st.write("Recyclable: Yes")
            st.write("Environmental Impact: Low pollution")
            st.write("Suggestion: Reuse glass containers")
            st.write("Eco Score: High")

        elif prediction == "Paper":
            st.write("Material:", prediction)
            st.write("Recyclable: Yes")
            st.write("Environmental Impact: Biodegradable")
            st.write("Suggestion: Use recycled paper products")
            st.write("Eco Score: High")

        elif prediction == "Metal":
            st.write("Material:", prediction)
            st.write("Recyclable: Highly recyclable")
            st.write("Environmental Impact: Durable and reusable")
            st.write("Suggestion: Prefer metal containers")
            st.write("Eco Score: High")

        else:
            st.write("Material: Unknown")
            st.write("Recyclable: Unknown")
            st.write("Environmental Impact: Needs further analysis")
            st.write("Suggestion: Choose eco-friendly materials when possible")
            st.write("Eco Score: Medium")
