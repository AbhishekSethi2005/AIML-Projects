from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

for model in genai.list_models():
    print(model.name)

print("KEY = ", os.getenv("GOOGLE_API_KEY"))
