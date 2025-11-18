from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Configure API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ------------ Gemini Vision Function -------------
def get_gemini_response(prompt, image_parts):
    model = genai.GenerativeModel("models/gemini-2.0-flash")

    response = model.generate_content(
        [
            prompt,
            *image_parts
        ]
    )
    return response.text

# ------------ Image Bytes Converter -------------
def input_image_setup(uploaded_file):
    if uploaded_file is None:
        raise FileNotFoundError("No file uploaded")

    bytes_data = uploaded_file.getvalue()

    return [
        {
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }
    ]

# ------------ Streamlit UI -------------
st.set_page_config(page_title="Nutritionist AI Doctor", layout="centered")

# Model Header
st.markdown("<h2 style='text-align:center; color:#4CAF50;'>🤖 Gemini 2.0 Flash – Nutritionist AI Model</h2>", unsafe_allow_html=True)

# Project Name
st.markdown("<h1 style='text-align:center;'>🥗 Nutritionist Generative AI Doctor</h1>", unsafe_allow_html=True)
st.write("---")

# 📌 About the Project
st.markdown("### 📘 What is this Project?")
st.write("""
This is an AI-powered health assistant that identifies food items from an image
and generates a complete nutritional breakdown including calories,
macros, and health recommendations.
""")

# 📌 How it works
st.markdown("### ⚙️ How It Works?")
st.write("""
1. You upload a food image.  
2. The image is processed using **Gemini’s Vision Model**.  
3. The AI detects all food items individually.  
4. It estimates calories + provides a nutrition report.  
5. You receive a health-friendly breakdown instantly.
""")

# 📌 Aim
st.markdown("### 🎯 Aim of This App")
st.write("""
To help users understand what they eat by using AI for automated nutrition detection,
calorie calculation, and healthier decision-making.
""")

# 📌 Advantages
st.markdown("### 🌟 Advantages of this AI Nutritionist")
st.write("""
- Instant calorie estimation  
- Works with any food image  
- Helps in maintaining diet & fitness goals  
- Reduces dependency on manual calorie checking  
- Useful for students, athletes, diabetic patients, and fitness lovers  
""")

st.write("---")

# Upload section
st.markdown("### 📤 Upload Your Food Image")
uploaded_file = st.file_uploader("Upload a food image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Food Image", use_container_width=True)

# Chatbox text
input_text = st.text_input("💬 Add extra instructions (optional): ")

submit = st.button("🍎 Analyze Calories")

# Nutrition Prompt
nutrition_prompt = """
You are a professional nutritionist. Analyze the food items in the uploaded image,
identify each item, and calculate approximate calories.

Return the result in this format:

1. Item Name - calories
2. Item Name - calories
3. Item Name - calories

Total Calories: XYZ
"""

# On submit
if submit:
    try:
        image_parts = input_image_setup(uploaded_file)
        final_prompt = nutrition_prompt + "\n\n" + input_text

        response = get_gemini_response(final_prompt, image_parts)

        st.write("---")
        st.markdown("## 🍽️ Nutrition Breakdown")
        st.write(response)

    except Exception as e:
        st.error(f"Error: {str(e)}")
