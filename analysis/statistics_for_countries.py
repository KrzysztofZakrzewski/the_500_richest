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

#==============
# Compute correlation matrix for countrys
#==============
def compute_country_correlation(df_country: pd.DataFrame) -> pd.DataFrame:
    """
    Compute correlation matrix for numeric columns only.
    """
    df_corr = df_country.drop(
        columns=["Name", "Rank", "Country / Region", "Industry"],
        errors="ignore"
    )

    return df_corr.corr()

#==============
# Compute Total net worth vs YTD change
#==============
def prepare_scatter_country(df_country: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare data for scatter plot: Total net worth vs YTD change.
    """
    # Kopiujemy dane (żeby nie zmieniać oryginału)
    df_scatter = df_country.copy()

    # Opcjonalnie można filtrować lub przetwarzać np. brakujące wartości
    df_scatter = df_scatter.dropna(subset=['Total net worth', '$ YTD change'])

    return df_scatter

#==============
# Compute industry distribution
#==============
def compute_industry_distribution_country(df: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    """
    Compute counts and percentages of billionaires per industry.
    
    Parameters
    ----------
    df : pd.DataFrame
        Country filtered dataframe.
    
    Returns
    -------
    counts : pd.Series
        Number of billionaires per industry.
    percentage : pd.Series
        Percentage of billionaires per industry.
    """
    counts = df['Industry'].value_counts()
    percentage = (counts / counts.sum() * 100).round(1)
    return counts, percentage

#==============
# Boxplot of Total Net Worth of Billionaires
#==============
def prepare_boxplot_data_country(
    df_country: pd.DataFrame,
    column: str
) -> pd.DataFrame:
    """
    Prepare data for a boxplot for a single country.

    Currently returns a shallow copy of the DataFrame,
    but exists for consistency and future extensions
    (e.g. filtering, outlier handling).

    Parameters
    ----------
    df_country : pd.DataFrame
        DataFrame filtered to a single country.
    column : str
        Column to be used for the boxplot.

    Returns
    -------
    pd.DataFrame
        Prepared DataFrame for visualization.
    """
    return df_country[[column]].copy()

# ==========
# Boxplot of Total Net Worth of Billionaires by Industry by Industry
# ==========
def prepare_industry_boxplot_data_country(
    df_country: pd.DataFrame,
    value_column: str,
    category_column: str
) -> pd.DataFrame:
    """
    Prepare data for an industry-level boxplot for a single country.

    Parameters
    ----------
    df_country : pd.DataFrame
        DataFrame filtered to a single country.
    value_column : str
        Numerical column used for boxplot values (e.g. total net worth).
    category_column : str
        Categorical column used for grouping (e.g. industry).

    Returns
    -------
    pd.DataFrame
        Prepared DataFrame for visualization.
    """
    return df_country[[value_column, category_column]].copy()

import pandas as pd

# ==========
# Prepare data for an industry-level boxplot of last net worth change
# ==========
def prepare_industry_boxplot_last_change_country(
    df_country: pd.DataFrame,
    value_column: str = "$ Last change",
    category_column: str = "Industry"
) -> pd.DataFrame:
    """
    Prepare data for an industry-level boxplot of last net worth change
    for a single country.

    Parameters
    ----------
    df_country : pd.DataFrame
        DataFrame filtered to a single country.
    value_column : str
        Column representing last net worth change.
    category_column : str
        Column representing industry categories.

    Returns
    -------
    pd.DataFrame
        Prepared DataFrame for boxplot visualization.
    """
    return df_country[[value_column, category_column]].copy()


# ==========
# Prepare data for Total net worth
# ==========
def prepare_net_worth_histogram_country(
    df_country: pd.DataFrame,
    column: str = "Total net worth"
) -> pd.Series:
    """
    Prepare data for histogram of total net worth for a single country.

    Parameters
    ----------
    df_country : pd.DataFrame
        DataFrame filtered for a single country.
    column : str, default "Total net worth"
        Column containing net worth values.

    Returns
    -------
    pd.Series
        Series with net worth values (NaNs dropped).
    """
    return df_country[column].dropna()
