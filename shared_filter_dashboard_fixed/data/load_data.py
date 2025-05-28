import streamlit as st
import pandas as pd
import os

@st.cache_data
def load_well_data():
    path = os.path.join(os.path.dirname(__file__), "..", "Updated_Merged_Data_with_API_and_Location.csv")
    try:
        df = pd.read_csv(path)
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
        df.rename(columns={
            "well_name": "well_name",
            "rig": "rig",
        }, inplace=True)
        return df
    except Exception as e:
        st.error(f"❌ Failed to load data: {e}")
        return pd.DataFrame(columns=["well_name", "rig", "depth"])
