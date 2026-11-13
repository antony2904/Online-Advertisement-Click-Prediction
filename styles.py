import streamlit as st

def apply_theme():
    st.markdown("""
    <style>
    .stApp {
      background: radial-gradient(ellipse at 12% 0%, rgba(239,51,64,.13), transparent 34%),
                  radial-gradient(ellipse at 90% 10%, rgba(239,51,64,.07), transparent 28%), #08090d;
      color: #f5f6fa;
    }
    [data-testid="stHeader"] {background: rgba(8,9,13,.82);}
    [data-testid="stSidebar"] {background:#0d0f15;border-right:1px solid rgba(255,255,255,.09);}
    [data-testid="stSidebar"] * {color:#eef0f5;}
    h1,h2,h3 {color:#fff !important;letter-spacing:-.035em;}
    p,label,.stMarkdown {color:#c5c8d1;}
    [data-testid="stMetric"] {
      background:linear-gradient(145deg,#191c26,#101219);
      border:1px solid rgba(239,51,64,.24);border-radius:15px;
      padding:18px;box-shadow:0 8px 26px rgba(0,0,0,.2);
    }
    [data-testid="stMetricLabel"] {color:#aeb3c0 !important;}
    [data-testid="stMetricValue"] {color:#fff !important;font-weight:800 !important;}
    .stButton>button,.stDownloadButton>button, [data-testid="stFormSubmitButton"] button {
      background:linear-gradient(100deg,#d91f2b,#f04450);color:white !important;
      border:0;border-radius:10px;font-weight:700;
    }
    .stTabs [data-baseweb="tab"] {color:#b9bdc8;background:#141720;}
    .stTabs [aria-selected="true"] {color:#fff !important;border-bottom:3px solid #ef3340 !important;}
    .hero-card {
      background:linear-gradient(120deg,rgba(239,51,64,.18),rgba(20,23,32,.96) 58%);
      border:1px solid rgba(239,51,64,.28);border-radius:18px;
      padding:24px 26px;margin:8px 0 22px;
    }
    .hero-eyebrow {color:#ff6973;text-transform:uppercase;letter-spacing:.16em;font-size:.72rem;font-weight:800;}
    .hero-title {color:#fff;font-size:1.8rem;font-weight:850;margin:7px 0 4px;}
    .hero-subtitle {color:#b8bdc9;margin:0;}
    #MainMenu,footer {visibility:hidden;}
    </style>
    """, unsafe_allow_html=True)
