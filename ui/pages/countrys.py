import streamlit as st
import pandas as pd

# =============
# Render Tabs
# =============

def render_countries(df: pd.DataFrame) -> None:
    """
    Render the Countries section with tab-based views for selected countries.

    Creates a separate tab for each country and renders the corresponding
    country-specific analysis using a shared view function.

    Parameters
    ----------
    df : pd.DataFrame
        Full dataset containing data for all countries.
    """
    st.title("Countries")

    countries = {
        "USA": "United States",
        "China": "China",
        "India": "India",
        "Russia": "Russia",
        "Germany": "Germany",
    }

    tabs = st.tabs(countries.keys())

    for tab, country_name in zip(tabs, countries.values()):
        with tab:
            render_country_view(df, country_name)

# =============
# Render Single Country In Individual tab
# =============

def render_country_view(df: pd.DataFrame, country: str) -> None:
    """
    Render analysis and overview for a single country.

    Filters the input DataFrame by the given country and displays
    country-specific data and visualizations.

    Parameters
    ----------
    df : pd.DataFrame
        Full dataset containing multiple countries.
    country : str
        Country name used to filter the dataset (value from 'Country / Region').
    """
    st.markdown(
        f"<h3>General Overview of the Data for {country}</h3>",
        unsafe_allow_html=True
    )

    df_country = df[df["Country / Region"] == country]

    if df_country.empty:
        st.warning("No data available.")
        return

    st.dataframe(df_country)