import streamlit as st
import joblib

# Modelni yuklash
model = joblib.load('phishing_model.pkl')

# Dastur sarlavhasi
st.title("Phishing Email Aniqlash Dasturi")

# Email matnini kiritish
email_text = st.text_area("Email matnini kiriting:")

# Tekshirish tugmasi
if st.button("Tekshirish"):
    # Modeldan natijani olish
    prediction = model.predict([email_text])
    confidence = model.decision_function([email_text])  # Ishonch darajasini olish

    # Natijani ko'rsatish
    if prediction[0] == 1:  # 1 - Phishing Email
        st.error("Bu phishing email!")
    else:
        st.success("Bu xavfsiz email!")

    # Ishonch darajasini ko'rsatish
    st.write(f"Ishonch darajasi: {confidence[0]:.2f}")

















