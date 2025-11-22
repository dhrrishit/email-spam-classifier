import streamlit as st
import os
import sys
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.model import train_model, predict_message

# Page Config
st.set_page_config(
    page_title="Spam Detector AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    .main-header {
        font-size: 3rem;
        font-weight: 700;
        color: #1e3a8a;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }

    .sub-header {
        font-size: 1.2rem;
        color: #4b5563;
        text-align: center;
        margin-bottom: 2rem;
    }

    .stTextArea textarea {
        border-radius: 12px;
        border: 2px solid #e5e7eb;
        padding: 1rem;
        font-size: 1rem;
        transition: border-color 0.3s ease;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }

    .stTextArea textarea:focus {
        border-color: #3b82f6;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
    }

    .stButton button {
        width: 100%;
        border-radius: 12px;
        background: linear-gradient(to right, #3b82f6, #2563eb);
        color: white;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        border: none;
        transition: transform 0.1s ease, box-shadow 0.3s ease;
    }

    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.3);
    }

    .result-card {
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        animation: fadeIn 0.5s ease-out;
        margin-top: 2rem;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
    }

    .spam-card {
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        border: 2px solid #ef4444;
        color: #991b1b;
    }

    .ham-card {
        background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%);
        border: 2px solid #22c55e;
        color: #166534;
    }

    .result-title {
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }

    .confidence-score {
        font-size: 1.1rem;
        opacity: 0.9;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e5e7eb;
    }
</style>
""", unsafe_allow_html=True)

import pandas as pd
from src.analytics import get_data_distribution, plot_pie_chart, plot_wordcloud
from src.history import log_query, get_history

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2058/2058768.png", width=80)
    st.title("Spam Detector")
    st.markdown("---")
    st.markdown("""
    ### 🤖 How it works
    This AI uses a **Support Vector Machine (SVM)** trained on over 5,000 SMS messages to detect spam with high accuracy.
    
    ### 📊 Stats
    - **Accuracy**: 97.6%
    - **Precision**: 96.2%
    
    ### 👨‍💻 Developer
    Built for **VITyarthi Project**
    """)
    st.markdown("---")
    st.caption("v2.0.0 | Powered by Scikit-learn")

tab1, tab2, tab3 = st.tabs(["🏠 Home", "📊 Analytics", "📜 History"])

with tab1:
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown('<div class="main-header">🛡️ Spam Detector AI</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">Keep your inbox safe. Paste a message below to check if it\'s spam.</div>', unsafe_allow_html=True)

        input_sms = st.text_area("Message Text", height=150, placeholder="e.g., Congratulations! You've won a $1000 gift card...")

        if st.button('Analyze Message'):
            if not input_sms:
                st.warning("⚠️ Please enter a message to analyze.")
            else:
                if not os.path.exists('model.pkl'):
                    with st.status("⚙️ System Initializing...", expanded=True) as status:
                        st.write("Loading dataset...")
                        time.sleep(0.5)
                        st.write("Training SVM model...")
                        train_model()
                        status.update(label="✅ System Ready!", state="complete", expanded=False)
                
                with st.spinner('🔍 Analyzing patterns...'):
                    time.sleep(0.6)
                    try:
                        prediction, proba = predict_message(input_sms)
                        confidence = proba[1] if prediction == 1 else proba[0]
                        
                        log_query(input_sms, prediction, confidence)
                        
                        if prediction == 1:
                            st.markdown("""
                            <div class="result-card spam-card">
                                <div class="result-title">🚨 SPAM DETECTED</div>
                                <div class="confidence-score">Confidence: {:.1f}%</div>
                            </div>
                            """.format(confidence*100), unsafe_allow_html=True)
                        else:
                            st.balloons()
                            st.markdown("""
                            <div class="result-card ham-card">
                                <div class="result-title">✅ SAFE MESSAGE</div>
                                <div class="confidence-score">Confidence: {:.1f}%</div>
                            </div>
                            """.format(confidence*100), unsafe_allow_html=True)
                            
                    except Exception as e:
                        st.error(f"An error occurred: {e}")

with tab2:
    st.header("📊 Dataset Analytics")
    try:
        df = pd.read_csv('data/spam.csv', encoding='latin-1')
        df = df.iloc[:, :2]
        df.columns = ['target', 'text']
        df['target'] = df['target'].map({'ham': 0, 'spam': 1})
        from src.preprocessing import transform_text
        df['transformed_text'] = df['text'].apply(transform_text)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Distribution")
            counts = get_data_distribution(df)
            fig = plot_pie_chart(counts)
            st.pyplot(fig)
            
        with col2:
            st.subheader("Spam Word Cloud")
            fig = plot_wordcloud(df, 1)
            st.pyplot(fig)

    except Exception as e:
        st.error(f"Could not load analytics: {e}")

with tab3:
    st.header("📜 Recent Queries")
    history_df = get_history()
    if not history_df.empty:
        st.dataframe(history_df, use_container_width=True)
    else:
        st.info("No queries yet.")
