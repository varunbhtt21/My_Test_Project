import google.generativeai as genai
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

env_api_key = os.getenv("GOOGLE_API_KEY")

# AI Setup
genai.configure(api_key=env_api_key)
model = genai.GenerativeModel("gemini-1.5-pro")

def ask_gemini(question):
    response = model.generate_content(question)
    return response.text