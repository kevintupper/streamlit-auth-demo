import streamlit as st
import utils

utils.setup_page("Home")


st.write("Welcome to the Azure AI Demo Platform!")

st.write("User info:", st.session_state.user_info)
