import streamlit as st

# Set page title
st.title("User Information Form")

# Create a form
with st.form("user_info_form"):
    # Input fields
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=0, max_value=120)
    gender = st.selectbox("Select your gender", ["Male", "Female", "Other", "Prefer not to say"])
    
    # New fields
    pincode = st.text_input("Enter your pincode", max_chars=6)
    hobbies = st.multiselect(
        "Select your hobbies",
        ["Reading", "Sports", "Music", "Cooking", "Travel", "Photography", "Gaming", "Art", "Dancing", "Other"]
    )
    
    # Submit button
    submitted = st.form_submit_button("Submit")
    
    # Display information when form is submitted
    if submitted:
        st.write("### Submitted Information:")
        st.write(f"**Name:** {name}")
        st.write(f"**Age:** {age}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Pincode:** {pincode}")
        st.write("**Hobbies:**")
        for hobby in hobbies:
            st.write(f"- {hobby}")

