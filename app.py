import streamlit as st
import streamlit.components.v1 as components
from config import get_config
from pages import free_tier, premium_tier
from utils.session_manager import initialize_session_state
from utils.payment_handler import handle_payment_success

# Page configuration
st.set_page_config(
    page_title="ProProofread Hub",
    page_icon="✏️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load configuration
config = get_config()

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .tier-badge {
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .premium-badge {
        background-color: #ffd700;
        color: #000;
    }
    .free-badge {
        background-color: #e0e0e0;
        color: #333;
    }
    .feature-box {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background-color: #f5f5f5;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
initialize_session_state()

# Check for payment success
query_params = st.query_params
if "payment" in query_params and query_params["payment"] == "success":
    handle_payment_success()

# Main application layout
st.markdown('<p class="main-header">✏️ ProProofread Hub</p>', unsafe_allow_html=True)
st.markdown("Your AI-powered and human-verified text proofreading platform")

# Sidebar with tier information and subscription management
with st.sidebar:
    st.header("📊 Account & Subscription")
    
    if st.session_state.is_premium:
        st.markdown('<div class="tier-badge premium-badge">⭐ Premium Access</div>', unsafe_allow_html=True)
        st.success("Unlimited access to all features")
        
        # Show subscription info
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Status", "Active")
        with col2:
            st.metric("Tier", "Premium")
        
        if st.button("📋 View Subscription Details"):
            st.info("""
            **Premium Features:**
            - Unlimited AI proofreading
            - Unlimited human reviews
            - Plagiarism detection
            - Expert escalation
            - Advanced tone calibration
            - Priority support
            """)
        
        if st.button("🚪 Switch to Free Tier Demo"):
            st.session_state.is_premium = False
            st.query_params.clear()
            st.rerun()
    else:
        st.markdown('<div class="tier-badge free-badge">Free Tier</div>', unsafe_allow_html=True)
        st.info(f"Human Reviews: {st.session_state.human_chances}/5 | AI Checks: {st.session_state.ai_chances}/5")
        
        st.subheader("🚀 Upgrade to Premium")
        st.write("Unlock unlimited access and advanced features")
        
        # Payment options
        payment_method = st.radio("Choose Payment Method:", ["PayPal", "Stripe"], key="payment_method")
        tier_option = st.selectbox("Select Tier:", 
                                   ["Full Access ($10 USD)", "24-Hour Pass ($2 USD)"])
        
        if payment_method == "PayPal":
            if st.button("💳 Pay with PayPal"):
                st.info("Redirecting to PayPal checkout...")
        else:
            if st.button("💳 Pay with Stripe"):
                st.info("Redirecting to Stripe checkout...")
    
    st.divider()
    st.subheader("📚 Resources")
    if st.button("❓ Help & FAQ"):
        st.info("""
        **Frequently Asked Questions:**
        
        Q: How long does human review take?
        A: Typically 24-48 hours for community reviews.
        
        Q: Can I cancel my subscription?
        A: Yes, anytime from your account settings.
        
        Q: Is my text private?
        A: All submissions are encrypted and kept confidential.
        """)
    
    if st.button("📧 Contact Support"):
        st.info("Email: support@proproofread.hub")

# Main content area
if st.session_state.is_premium:
    premium_tier.render()
else:
    free_tier.render()

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #888; font-size: 0.9rem;">
    <p>ProProofread Hub © 2024 | Powered by AI & Community | <a href="#">Privacy Policy</a> | <a href="#">Terms of Service</a></p>
</div>
""", unsafe_allow_html=True)
