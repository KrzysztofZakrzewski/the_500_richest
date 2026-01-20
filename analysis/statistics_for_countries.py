import pandas as pd

#==============
# Compute industry distribution
#==============
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

#==============
# Compute total net worth by industry
#==============
def compute_total_net_worth_by_industry(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Compute total net worth by industry.

    Returns DataFrame with:
    - Industry
    - Total net worth (in USD billions)
    - Percentage share
    """
    result = (
        df.groupby("Industry", as_index=False)["Total net worth"]
        .sum()
        .sort_values(by="Total net worth", ascending=False)
        .reset_index(drop=True)
    )

    result["Total net worth"] = (result["Total net worth"] / 1e9).round(1)
    result["Percentage"] = (
        result["Total net worth"] / result["Total net worth"].sum() * 100
    ).round(1)

    return result

#==============
# Compute YTD income by by industry
#==============
def compute_ytd_income_by_industry(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute YTD net income by industry.

    Returns DataFrame with:
    - Industry
    - YTD change (USD billions)
    - Percentage contribution
    """
    result = (
        df.groupby("Industry", as_index=False)["$ YTD change"]
        .sum()
        .sort_values(by="$ YTD change", ascending=False)
        .reset_index(drop=True)
    )

    result["$ YTD change"] = (
        pd.to_numeric(result["$ YTD change"], errors="coerce")
        .fillna(0)
        / 1e9
    ).round(2)

    total_sum = result["$ YTD change"].sum()
    result["Percentage"] = (
        result["$ YTD change"] / total_sum * 100
    ).round(1)

    return result
