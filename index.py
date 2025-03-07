import re
import streamlit as st

# Page Styling
st.set_page_config(
    page_title="Password Strength Checker by Haroon Rasheed",
    page_icon="🔐",
    layout="centered",
)

# Custom CSS
custom_css = """
<style>
  .main {
      text-align: center;
  }

  .stTextInput {
      width: 60% !important;
      margin: auto;
      display: block;
  }

  .stButton button {
      background-color: #4CAF50;
      color: white;
      padding: 10px 20px;
      border: none;
      cursor: pointer;
      border-radius: 5px;
  }

  .stButton button:hover {
      background-color: #45a049;
  }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Page title and description
st.title("👁‍📛 Password Strength Checker")
st.write("Enter a password to check its strength. 😈")

# Function: Password Strength Checker
def check_password_strength(password):
    score = 0
    feedback = []

    # Check for length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one number.")

    # Check for special characters
    if re.search(r'[@$!%*?&]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (@, $, !, %, *, ?, &).")

    return score, feedback

# User input field
password = st.text_input("🔑 Enter your password", type="password")

if st.button("Check Strength"):
    if password:
        score, feedback = check_password_strength(password)

        # Strength Evaluation
        if score == 5:
            st.success("✅ Strong Password! 🔥")
        elif score >= 3:
            st.warning("⚠️ Moderate Password! Try making it stronger.")
        else:
            st.error("❌ Weak Password! Please follow the suggestions below.")

        # Show Feedback
        for suggestion in feedback:
            st.write(suggestion)
    else:
        st.error("❌ Please enter a password.")
