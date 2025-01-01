import streamlit as st
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the model
model = joblib.load('phishing_model.pkl')

# Load the vectorizer (make sure to save and load the same vectorizer used during training)
vectorizer = joblib.load('vectorizer.pkl')  # Assuming you saved your vectorizer

# Application title
st.title("Phishing Email Detection App")

# Input email text
email_text = st.text_area("Enter the email text:")

# Check button
if st.button("Check"):
    # Convert the email text to the same format used during training
    email_vector = vectorizer.transform([email_text])  # Transform the text to a numeric format

    # Get prediction from the model
    prediction = model.predict(email_vector)  # Use the transformed input
    confidence = model.decision_function(email_vector)  # Get confidence level

    # Display the result
    if prediction[0] == 1:  # 1 - Phishing Email
        st.error("This is a phishing email!")
    else:
        st.success("This is a safe email!")

    # Show confidence level
    st.write(f"Confidence level: {confidence[0]:.2f}")