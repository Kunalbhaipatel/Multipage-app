
import streamlit as st
from components.filter_bar import filter_controls
from data.load_data import load_well_data

st.set_page_config(page_title="Rig Dashboard", layout="wide")
st.title("🏠 Drilling Performance Dashboard")

# Load data and apply filters
df = load_well_data()
filter_controls(df['Well_Name'].unique(), df['Rig'].unique())

st.success("Select a page from the sidebar to explore detailed modules.")
