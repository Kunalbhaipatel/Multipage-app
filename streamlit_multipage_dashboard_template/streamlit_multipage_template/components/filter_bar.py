
import streamlit as st

def filter_controls(wells, rigs):
    st.sidebar.title("🔎 Filters")
    well = st.sidebar.selectbox("Select Well", wells, key="selected_well")
    rig = st.sidebar.selectbox("Select Rig", rigs, key="selected_rig")
    st.session_state.selected_well = well
    st.session_state.selected_rig = rig
