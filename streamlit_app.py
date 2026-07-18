
import streamlit as st
import google.generativeai as genai

# API Key को Secrets से उठा रहे हैं
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

system_instruction = """
You are an expert Agriculture Assistant named AgriNexus Tech. 
Help farmers with crop management, soil health, and farming techniques in a friendly manner. 
Respond clearly in simple Hindi or English as requested.
"""

st.title("🧑‍🌾 AgriNexus Tech - स्मार्ट किसान मित्र")
st.write("खेती, मौसम, और फसलों से जुड़ा कोई भी सवाल पूछें!")

user_input = st.text_input("आपका सवाल यहाँ लिखें:")

if st.button("जवाब पाएं"):
    if user_input:
        try:
            model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                system_instruction=system_instruction
            )
            response = model.generate_content(user_input)
            st.success(response.text)
        except Exception as e:
            st.error(f"कुछ गड़बड़ हो गई: {e}")
    else:
        st.error("कृपया पहले अपना सवाल लिखें!")
                
