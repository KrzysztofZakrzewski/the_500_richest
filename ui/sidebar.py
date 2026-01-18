import streamlit as st

#==============
# RENDER SIDEBAR
#==============

def render_sidebar() -> str:
    """Render sidebar navigation and return selected section."""
    with st.sidebar:
        return st.selectbox(
            "Wybierz przykład do pokazania",
            [
                "About",
                "Global analysis",
                "Countries",
            ],
        )
