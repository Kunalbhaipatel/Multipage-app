
import streamlit as st
import pandas as pd

@st.cache_data
def load_well_data():
    # Replace with actual data file path or API
    return pd.DataFrame({
        "Well_Name": ["Alpha", "Bravo", "Charlie"],
        "Rig": ["Rig-1", "Rig-2", "Rig-3"],
        "Depth": [10000, 8500, 9000]
    })
