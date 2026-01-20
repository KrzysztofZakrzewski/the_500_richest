import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# import statsmodels.api as sm
import io

from analysis.data_overview import compute_basic_overview
from analysis.statistics_for_countries import *
from ui.components.data_overview import render_basic_country_overview

from visualization.plots_countrys import *

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


    # ===== BASIC OVERVIEW =====
    # --- COMPUTE
    overview = compute_basic_overview(df_country)
    # --- RENDER
    st.markdown(f'<h3 ># STEP 1: General Overview of the Data for US{country}</h3>', unsafe_allow_html=True)
    render_basic_country_overview(overview, info_str)

    st.markdown("<h3>STEP 2: Single Variable Analysis</h3>", unsafe_allow_html=True)
    # ===== INDUSTY DISTRIBUTION =====
    # --- COMPUTE
    industry_df = compute_industry_distribution(df_country)
    # --- RENDER
    st.markdown(f"<h4>Barplot of Billionaires by Industry in {country}</h4>", unsafe_allow_html=True)
    render_industry_barplot_countrys(industry_df, country)

    # ===== TOTAL NET WORTH =====
    # --- COMPUTE
    net_worth_df = compute_total_net_worth_by_industry(df_country)
    # --- RENDER
    st.markdown(f'<h4>Barplot for Billionaires Total Net Worth by Industry in {country} (USD Billion)</h4>', unsafe_allow_html=True)
    fig = plot_total_net_worth_by_industry(net_worth_df, country)
    st.pyplot(fig)

    # ===== YTD NET INCOME OF MILLIONAiRES IN GIVEN INDUSTRY=====
    # --- COMPUTE
    ytd_df = compute_ytd_income_by_industry(df_country)
    # --- RENDER
    st.markdown(f'<h4>YTD net income of Millionaires in a given industry in {country}</h4>', unsafe_allow_html=True)
    fig = plot_ytd_income_by_industry(ytd_df, country)
    st.pyplot(fig)

    # ===== CORELATIONS
    st.markdown('<h3 ># STEP 3: Correlations</h3>', unsafe_allow_html=True)

    st.markdown(f'<h4>Correlation Matrix for bilioners in {country}</h4>', unsafe_allow_html=True)
    # --- COMPUTE
    corr_matrix = compute_country_correlation(df_country)
    # --- RENDER
    st.dataframe(corr_matrix)
    fig = plot_country_correlation(corr_matrix, title=f"Correlation Matrix – {country}")
    st.pyplot(fig)
