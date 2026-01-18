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


# --- Calculate the number of records fer industry
@st.cache_data
def compute_industry_counts(df: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    """
    Compute number and percentage of billionaires per industry.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataset containing the 'Industry' column.

    Returns
    -------
    tuple[pd.Series, pd.Series]
        Counts and percentage share per industry.
    """
    counts = df["Industry"].value_counts()
    percentage = (counts / len(df)) * 100
    return counts, percentage

# --- Aggregate total net worth per industry and sort descending
@st.cache_data
def aggregate_net_worth_by_industry(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate total net worth per industry and sort descending.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing 'Industry' and 'Total net worth'.

    Returns
    -------
    pd.DataFrame
        Aggregated DataFrame sorted by total net worth.
    """
    result = df.groupby("Industry", as_index=False)["Total net worth"].sum()
    result = result.sort_values(by="Total net worth", ascending=False).reset_index(drop=True)
    return result

# --- Compute total net worth and percentage share by industry.
@st.cache_data
def compute_total_net_worth_by_industry(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Compute total net worth and percentage share by industry.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataset containing 'Industry' and 'Total net worth' columns.

    Returns
    -------
    pd.DataFrame
        DataFrame with total net worth (in billions USD) and percentage share
        per industry.
    """
    result = df.copy()

    result["Total net worth"] = (result["Total net worth"] / 1e9).round(1)
    result["Percentage"] = (
        result["Total net worth"] / result["Total net worth"].sum() * 100
    ).round(1)

    return result

@st.cache_data
def aggregate_ytd_net_income(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate Year-to-Date net income by industry and sort descending.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing 'Industry' and '$ YTD change' columns.

    Returns
    -------
    pd.DataFrame
        Aggregated DataFrame sorted by '$ YTD change'.
    """
    result = df.groupby('Industry', as_index=False)['$ YTD change'].sum()
    result = result.sort_values(by='$ YTD change', ascending=False).reset_index(drop=True)
    return result


@st.cache_data
def compute_ytd_net_income(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and compute Year-to-Date net income by industry.

    Converts '$ YTD change' to numeric, normalizes to billions,
    and calculates percentage share per industry.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing '$ YTD change' and 'Industry' columns.

    Returns
    -------
    pd.DataFrame
        DataFrame with:
        - '$ YTD change' in billions
        - 'Percentage' of total YTD change per industry
    """
    result = df.copy()
    
    # Ensure numeric, replace NaN with 0
    result['$ YTD change'] = pd.to_numeric(result['$ YTD change'], errors='coerce').fillna(0)
    
    # Convert to billions
    result['$ YTD change'] = (result['$ YTD change'] / 1e9).round(2)
    
    # Percentage share
    total_sum = result['$ YTD change'].sum()
    result['Percentage'] = (result['$ YTD change'] / total_sum * 100).round(1)
    
    return result

# ===========
# CORRELATION MATRIX

def compute_correlation(df: pd.DataFrame, exclude_cols: list[str] = None) -> pd.DataFrame:
    """
    Compute correlation matrix for numeric columns of a DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame
    exclude_cols : list[str], optional
        Columns to exclude from correlation computation.

    Returns
    -------
    pd.DataFrame
        Correlation matrix
    """
    if exclude_cols is None:
        exclude_cols = ['Name', 'Rank', 'Country / Region', 'Industry']
    corr_df = df.drop(columns=exclude_cols)
    return corr_df.corr()


def detect_outliers_iqr(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """
    Detect outliers in numerical columns using the IQR method.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.

    Returns
    -------
    dict[str, pd.DataFrame]
        Dictionary where keys are column names and values are DataFrames
        containing outlier rows for each column.
    """
    outliers = {}

    numeric_df = df.select_dtypes(include=['int64', 'float64'])

    for column in numeric_df.columns:
        Q1 = numeric_df[column].quantile(0.25)
        Q3 = numeric_df[column].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers[column] = df[
            (df[column] < lower_bound) | (df[column] > upper_bound)
        ]

    return outliers