import re
import streamlit as st

# Page styling (custom CSS)
st.markdown("""
    <style>
        body { background-color: black; color: white; }
        h1 { color: red; }
    </style>
""", unsafe_allow_html=True)

# Your Streamlit title
st.title("🔐 Welcome to My Streamlit App")

# Page title and description
st.write("Enter your password below to check its security level. 🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check if password is at least 8 characters long
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    # Check if password contains both upper and lower case letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password must have both uppercase and lowercase letters.")

    # Check if password contains at least one number
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one number (0-9).")

    # Check if password contains special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Display password strength results
    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure.")
    elif score == 3:
        st.info("🔺 **Moderate Password** - Consider improving security by adding more features.")
    else:
        st.info("❌ **Weak Password** - Follow the suggestions below to strengthen it.")

    # Display feedback
    if feedback:
        with st.expander("🔍 **Improve your password**"):
            for item in feedback:
                st.write(item)

# Take password input from the user
password = st.text_input("Enter your password:", type="password", help="Enter your password")

# Button to check strength
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")  # Show warning if password is empty




                 
                             


