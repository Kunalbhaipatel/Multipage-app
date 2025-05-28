import streamlit as st
import pandas as pd
import os

@st.cache_data
def load_well_data():
    path = os.path.join(os.path.dirname(__file__), "..", "Updated_Merged_Data_with_API_and_Location.csv")
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        st.error(f"❌ File not found: {path}")
        return pd.DataFrame(columns=["Well_Name", "Rig", "Depth"])
