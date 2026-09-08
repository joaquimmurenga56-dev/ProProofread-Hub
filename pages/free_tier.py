import streamlit as st

def render():
    """Render free tier dashboard"""
    st.subheader("📖 Free Tier Dashboard")
    st.markdown("Get started with our core proofreading features. Upgrade to Premium for unlimited access.")
    
    tab1, tab2 = st.tabs(["👥 Community Review", "🤖 AI Proofreader"])
    
    with tab1:
        render_community_review()
    
    with tab2:
        render_ai_proofreader()

def render_community_review():
    """Render community/human proofreading section"""
    st.write(f"**Remaining Slots:** {st.session_state.human_chances}/5")
    st.markdown("""
    Submit your text to our community of expert proofreaders. 
    Get detailed feedback on grammar, style, clarity, and tone.
    """)
    
    human_text = st.text_area(
        "Paste your text for community review:",
        key="free_human_input",
        height=200,
        placeholder="Enter your text here..."
    )
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.info("⏱️ Average review time: 24-48 hours")
    with col2:
        submit_button = st.button("📤 Submit for Review", key="submit_human")
    
    if submit_button:
        if st.session_state.human_chances > 0:
            if human_text.strip():
                st.session_state.human_chances -= 1
                st.success("✅ Your text has been submitted to the community queue!")
                st.info("You'll receive notifications when reviewers provide feedback.")
                st.rerun()
            else:
                st.warning("⚠️ Please enter some text before submitting.")
        else:
            st.error("❌ You've used all your free review slots. Upgrade to Premium for unlimited access.")
            if st.button("🚀 Upgrade Now"):
                st.session_state.is_premium = True
                st.rerun()

def render_ai_proofreader():
    """Render AI proofreading section"""
    st.write(f"**Remaining Checks:** {st.session_state.ai_chances}/5")
    st.markdown("""
    Get instant AI-powered proofreading with support for multiple languages and regional dialects.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        language = st.selectbox(
            "Target Language:",
            ["English", "Spanish", "French", "German", "Mandarin", "Japanese"],
            key="free_lang"
        )
    with col2:
        accent = st.selectbox(
            "Regional Dialect:",
            ["American", "British", "Australian", "Canadian", "Neutral"],
            key="free_accent"
        )
    
    ai_text = st.text_area(
        "Paste your text for AI proofreading:",
        key="free_ai_input",
        height=200,
        placeholder="Enter your text here..."
    )
    
    if st.button("✨ Run Proofreader", key="run_ai_free"):
        if st.session_state.ai_chances > 0:
            if ai_text.strip():
                st.session_state.ai_chances -= 1
                
                corrected_text = process_ai_proofreading(ai_text, language, accent)
                
                st.success("✅ Proofreading complete!")
                st.markdown("### Corrected Text:")
                st.text_area(
                    "Your proofread text:",
                    value=corrected_text,
                    height=200,
                    disabled=True,
                    key="free_output"
                )
                
                st.button("📋 Copy to Clipboard")
                st.rerun()
            else:
                st.warning("⚠️ Please enter some text before processing.")
        else:
            st.error("❌ You've used all your free AI checks. Upgrade to Premium for unlimited access.")
            if st.button("🚀 Upgrade Now", key="upgrade_ai"):
                st.session_state.is_premium = True
                st.rerun()

def process_ai_proofreading(text, language, accent):
    """Process text with AI proofreading (simulated)"""
    corrected = text.replace("teh", "the")
    corrected = corrected.replace("recieve", "receive")
    corrected = corrected.replace("occured", "occurred")
    corrected = corrected.replace("seperate", "separate")
    
    return f"[{language} - {accent} Dialect]\n\n{corrected}"
