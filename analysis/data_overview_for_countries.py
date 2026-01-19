import pandas as pd

def compute_basic_country_overview(df_country: pd.DataFrame) -> dict:
    """
    Compute basic descriptive statistics for a single country.

    Parameters
    ----------
    df_country : pd.DataFrame
        Filtered DataFrame containing data for a single country.

    Returns
    -------
    dict
        Dictionary with shape, nunique, total unique values
        and descriptive statistics.
    """
    return {
        "shape": df_country.shape,
        "nunique": df_country.nunique(),
        "unique_total": int(df_country.nunique().sum()),
        "describe": df_country.describe().T,
    }
