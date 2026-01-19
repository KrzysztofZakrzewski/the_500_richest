import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# import statsmodels.api as sm
import io

from analysis.data_overview import compute_basic_overview 
from ui.components.data_overview import render_basic_country_overview

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
        "Russia": "Russian Federation",
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

        # ===== INFO STRING =====
    buffer = io.StringIO()
    df_country.info(buf=buffer)
    info_str = buffer.getvalue()

    # ===== COMPUTE =====
    overview = compute_basic_overview(df_country)

    # ===== RENDER =====
    render_basic_country_overview(overview, info_str)