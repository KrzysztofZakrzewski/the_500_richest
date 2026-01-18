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

# --- Barplot of Numbers of Biloners for Industry
def industry_barplot(
    counts: pd.Series,
    percentage: pd.Series
) -> plt.Figure:
    """
    Create a bar plot showing the number of billionaires per industry.

    Bars are annotated with absolute counts and percentage share.

    Parameters
    ----------
    counts : pd.Series
        Number of records per industry.
    percentage : pd.Series
        Percentage share per industry.

    Returns
    -------
    matplotlib.figure.Figure
        Matplotlib figure object.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    bars = counts.plot(kind="bar", ax=ax, width=0.7)

    ax.set_ylim(0, counts.max() + 20)
    ax.set_title("Number of Billionaires in each Industry")
    ax.set_xlabel("Industry")
    ax.set_ylabel("Number of Billionaires")

    for bar, count, perc in zip(bars.patches, counts, percentage):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 5,
            f"{count}",
            ha="center",
            va="bottom",
            fontsize=12
        )
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() / 2,
            f"{perc:.1f}%",
            ha="center",
            va="center",
            fontsize=12
        )

    plt.xticks(rotation=65)
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()

    return fig
