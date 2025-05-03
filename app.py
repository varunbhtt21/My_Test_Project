import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configure the page
st.set_page_config(page_title="AI Joke Generator", page_icon="😄")
st.title("🤖 AI Joke Generator")
st.write("Get ready to laugh with AI-generated jokes!")

# Initialize Gemini
env_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=env_api_key)
model = genai.GenerativeModel("gemini-1.5-pro")

def generate_joke():
    prompt = "Tell me a funny, family-friendly joke. Keep it short and sweet."
    response = model.generate_content(prompt)
    return response.text

# Create a button to generate jokes
if st.button("Generate New Joke"):
    with st.spinner("Thinking of something funny..."):
        joke = generate_joke()
        st.write("---")
        st.write("### Your Joke:")
        st.write(joke)
        st.write("---")

# Add some styling
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
</style>
""", unsafe_allow_html=True)



