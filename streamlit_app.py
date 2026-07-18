
import streamlit as st
import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY") 

system_instruction = """
You are an expert Agriculture Assistant named AgriNexus Tech.
Help farmers with crop management, soil health, and farming techniques in a friendly manner. Respond clearly in Hindi or Hinglish.
"""

st.title("👨‍🌾 AgriNexus Tech - स्मार्ट किसान मित्र")
st.write("खेती, मौसम, ड्रोन तकनीक और फसलों की बीमारी से जुड़ा कोई भी सवाल पूछें।")

user_input = st.text_input("आपका सवाल यहाँ लिखें:")

if st.button("जवाब पाएं"):
    if user_input:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=system_instruction,
            tools=[{"google_search": {}}]
        )
        response = model.generate_content(user_input)
        st.success(response.text)
    else:
        st.error("कृपया पहले अपना सवाल लिखें!")
