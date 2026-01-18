import streamlit as st

#==============
# GLOBAL CSS
#==============

def inject_global_css() -> None:
    """Inject global CSS styles for the application."""
    st.markdown(
        """
        <style>
        .custom-title {
            font-size: 40px;
            width: 120%;
            text-align: start;
        }
        .custom-text {
            font-size: 18px;
            margin: 10px 0;
            text-align: justify;
        }
        </style>
        """,
        unsafe_allow_html=True
    )