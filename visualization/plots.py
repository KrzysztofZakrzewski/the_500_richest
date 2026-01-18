import matplotlib.pyplot as plt
import pandas as pd

# --- Barplot of Numbers of Biloners for region
def country_barplot(counts: pd.Series, percentage: pd.Series) -> plt.Figure:
    """
    Create a bar plot showing the number of billionaires per country.

    Each bar represents the total count of records for a given country.
    Values are annotated directly on the bars.

    Parameters
    ----------
    counts : pd.Series
        Number of records per country (indexed by country name).
    percentage : pd.Series
        Percentage share of records per country.

    Returns
    -------
    matplotlib.figure.Figure
        Matplotlib figure object containing the bar plot.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    bars = counts.plot(kind='bar', ax=ax)

    for bar, count, perc in zip(bars.patches, counts, percentage):
        ax.text(
            bar.get_x() + bar.get_width()/2,
            bar.get_height(),
            f'{count}',
            ha='center',
            va='bottom'
        )

    ax.set_title('Number of Bilioners in each Country / Region')
    ax.set_xlabel('Country / Region')
    ax.set_ylabel('Number of Bilioners')

    plt.xticks(rotation=90)
    plt.tight_layout()

    return fig