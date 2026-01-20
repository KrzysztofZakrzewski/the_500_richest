import pandas as pd

def compute_industry_distribution(df_country: pd.DataFrame) -> pd.DataFrame:
    """
    Compute number and percentage of billionaires by industry.

    Parameters
    ----------
    df_country : pd.DataFrame
        Data filtered to a single country.

    Returns
    -------
    pd.DataFrame
        DataFrame with columns:
        - Industry
        - Count
        - Percentage
    """
    counts = df_country["Industry"].value_counts()
    total = len(df_country)

    return pd.DataFrame({
        "Industry": counts.index,
        "Count": counts.values,
        "Percentage": (counts / total * 100).round(1)
    })
