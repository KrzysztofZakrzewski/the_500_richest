import streamlit as st
import pandas as pd

#==============
# LOAD DATA
#==============

@st.cache_data(show_spinner="Loading data...")
def load_data(path: str, sep: str = ',') -> pd.DataFrame:
    """
    Load dataset from CSV file.

    Parameters
    ----------
    path : str
        Path to the CSV file.
    sep : str, optional
        Column separator, by default ','

    Returns
    -------
    pd.DataFrame
        Loaded dataset.
    """
    # if not path.endswith(".csv"):
        # raise ValueError("Only CSV files are supported.")
    return pd.read_csv(path, sep=sep)