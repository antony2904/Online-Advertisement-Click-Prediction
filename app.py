import os
import pandas as pd
import streamlit as st
from styles import apply_theme
from data import prepare_data
from model import train_model
from pages import dashboard, explorer, visualizations, performance, prediction, about

st.set_page_config(page_title="AdClick Analytics", page_icon="📊", layout="wide")
apply_theme()
st.title("ADCLICK ANALYTICS")
st.caption("ONLINE ADVERTISEMENT CLICK PREDICTION / LOGISTIC REGRESSION")

FEATURES = ["Daily Time Spent on Site", "Age", "Area Income", "Daily Internet Usage", "Male"]
TARGET = "Clicked on Ad"

st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page", [
    "Dashboard", "Dataset Explorer", "Data Visualization",
    "Model Performance", "Predict Advertisement Click", "About Project"
])
st.sidebar.markdown("---")
st.sidebar.write("**Model:** Logistic Regression")
st.sidebar.write("**Target:** Clicked on Ad (0 / 1)")
uploaded = st.sidebar.file_uploader("Upload advertising.csv", type=["csv"])

if uploaded is not None:
    try:
        st.session_state["raw_df"] = pd.read_csv(uploaded)
        st.sidebar.success("Dataset uploaded")
    except Exception as exc:
        st.sidebar.error(f"Could not read CSV: {exc}")
elif "raw_df" not in st.session_state and os.path.exists("advertising.csv"):
    st.session_state["raw_df"] = pd.read_csv("advertising.csv")

if "raw_df" not in st.session_state:
    st.info("Upload advertising.csv using the sidebar to start.")
    st.markdown("### Required CSV columns")
    st.code("\\n".join(FEATURES + [TARGET]))
    st.stop()

try:
    df = prepare_data(st.session_state["raw_df"], FEATURES, TARGET)
    result = train_model(df, FEATURES, TARGET)
except Exception as exc:
    st.error(str(exc))
    st.stop()

routes = {
    "Dashboard": lambda: dashboard(df, result, TARGET),
    "Dataset Explorer": lambda: explorer(df),
    "Data Visualization": lambda: visualizations(df, FEATURES, TARGET),
    "Model Performance": lambda: performance(result),
    "Predict Advertisement Click": lambda: prediction(result, FEATURES),
    "About Project": lambda: about(FEATURES, TARGET)
}
routes[page]()
