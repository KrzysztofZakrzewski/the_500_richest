import pandas as pd
import streamlit as st

# --- Calculate the number of records
@st.cache_data
def country_counts_with_percentage(df: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    """
    Calculate the number of records (Bilioners) per country and their percentage share.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame containing a 'Country / Region' column.

    Returns
    -------
    tuple[pd.Series, pd.Series]
        - counts: number of records per country
        - percentage: percentage share of each country
    """
    counts = df['Country / Region'].value_counts()
    percentage = (counts / len(df)) * 100
    return counts, percentage