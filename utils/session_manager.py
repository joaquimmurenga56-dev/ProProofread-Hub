import streamlit as st
from datetime import datetime, timedelta

def initialize_session_state():
    """Initialize all session state variables"""
    if "human_chances" not in st.session_state:
        st.session_state.human_chances = 5
    
    if "ai_chances" not in st.session_state:
        st.session_state.ai_chances = 5
    
    if "is_premium" not in st.session_state:
        st.session_state.is_premium = False
    
    if "premium_expires" not in st.session_state:
        st.session_state.premium_expires = None
    
    if "user_id" not in st.session_state:
        st.session_state.user_id = None
    
    if "submission_history" not in st.session_state:
        st.session_state.submission_history = []
    
    if "payment_method" not in st.session_state:
        st.session_state.payment_method = None
    
    if "subscription_id" not in st.session_state:
        st.session_state.subscription_id = None

def is_premium_active():
    """Check if premium subscription is still active"""
    if not st.session_state.is_premium:
        return False
    
    if st.session_state.premium_expires:
        return datetime.now() < st.session_state.premium_expires
    
    return True

def activate_premium(duration_days=30, payment_method="unknown"):
    """Activate premium subscription"""
    st.session_state.is_premium = True
    st.session_state.premium_expires = datetime.now() + timedelta(days=duration_days)
    st.session_state.payment_method = payment_method
    st.session_state.human_chances = float('inf')
    st.session_state.ai_chances = float('inf')

def deactivate_premium():
    """Deactivate premium subscription"""
    st.session_state.is_premium = False
    st.session_state.premium_expires = None
    st.session_state.human_chances = 5
    st.session_state.ai_chances = 5
    st.session_state.subscription_id = None

def add_submission(text, submission_type, language, settings):
    """Add a submission to history"""
    submission = {
        "timestamp": datetime.now(),
        "type": submission_type,
        "text": text[:200] + "..." if len(text) > 200 else text,
        "language": language,
        "settings": settings,
        "status": "Processing"
    }
    st.session_state.submission_history.append(submission)

def reset_session():
    """Reset session to initial state"""
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    initialize_session_state()
