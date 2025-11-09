import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="AI in Cambodia",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
    }
    h1 {
        color: #1f77b4;
    }
    .highlight {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🤖 AI in Cambodia")
st.markdown("### Empowering Cambodia's Digital Future")

# Main sections
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ## Why AI in Cambodia?
    
    Cambodia is rapidly embracing digital transformation, with artificial intelligence playing a crucial role in its development. The growing tech ecosystem, young population, and government support create perfect conditions for AI innovation.
    """)

with col2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Flag_of_Cambodia.svg/1200px-Flag_of_Cambodia.svg.png", width=300)

# Key Areas
st.header("Key Areas of AI Development")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 🎓 Education
    - AI-powered learning platforms
    - Digital literacy programs
    - Language processing for Khmer
    """)

with col2:
    st.markdown("""
    ### 💼 Business
    - Smart automation solutions
    - Customer service chatbots
    - Fintech innovations
    """)

with col3:
    st.markdown("""
    ### 🌾 Agriculture
    - Smart farming systems
    - Crop yield prediction
    - Agricultural automation
    """)

# Statistics
st.header("AI Growth in Cambodia")

data = {
    'Year': [2023, 2024, 2025],
    'AI Startups': [15, 25, 40],
    'Tech Students': [5000, 7500, 10000],
    'Investment (M$)': [2, 5, 8]
}
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

# Contact Form
st.header("Get Involved")
with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    interest = st.selectbox(
        "Area of Interest",
        ["Education", "Business", "Agriculture", "Healthcare", "Other"]
    )
    message = st.text_area("Message")
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.success("Thanks for your interest! We'll get back to you soon.")

# Resources
st.header("Resources")
st.markdown("""
### Key Organizations
- Cambodia Academy of Digital Technology (CADT)
- Ministry of Posts and Telecommunications
- Khmer Technology Innovation Program
- Tech Startup Center Cambodia

### Events & Communities
- Cambodia Tech Expo
- AI Cambodia Meetup
- Digital Cambodia Conference
- Tech Women Cambodia
""")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ for Cambodia's tech community | © 2025 AI Cambodia")