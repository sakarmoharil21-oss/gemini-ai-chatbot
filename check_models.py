import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
API_KEY=os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise SystemExit("GEMINI_API_KEY not found")

genai.configure(api_key=API_KEY)

try:
    print("Fetching models...")
    for model in genai.list_models():
        if "generateContent" in model.supported_generation_methods:
            print(model.name)
except Exception as e:
    print("Error:", e)