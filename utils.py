# utils.py

import streamlit as st
import security

def setup_page(page_title):
    st.set_page_config(
        page_title=page_title,
        page_icon="👋",
    )

    if st.experimental_get_query_params().get('code'):
        security.handle_redirect()

    access_token = st.session_state.get('access_token')

    if access_token:
        user_info = security.get_user_info(access_token)
        st.session_state['user_info'] = user_info
        return True
    else:
        st.write("Please sign-in to use this app.")
        auth_url = security.get_auth_url()
        st.markdown(f"<a href='{auth_url}' target='_self'>Sign In</a>", unsafe_allow_html=True)
        st.stop()


