import pandas as pd
import streamlit as st

#  ==================
# Basic Overview For Global And Countrys
# ==================
@st.cache_data
def compute_basic_overview(df: pd.DataFrame) -> dict:
    """
    Compute basic descriptive statistics and structural information
    for a DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame to analyze.

    Returns
    -------
    dict
        Dictionary containing:
        - shape: tuple with number of rows and columns
        - nunique: number of unique values per column
        - unique_total: total number of unique values across all columns
        - describe: transposed descriptive statistics
    """
    return {
        "shape": df.shape,
        "nunique": df.nunique(),
        "unique_total": int(df.nunique().sum()),
        "describe": df.describe().T,
    }



