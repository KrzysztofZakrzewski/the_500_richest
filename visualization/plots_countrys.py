import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px

import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

# --- Render Industry Barplot
def render_industry_barplot_countrys(
    industry_df: pd.DataFrame,
    country_name: str
) -> None:
    """
    Render barplot of number of billionaires by industry.

    Parameters
    ----------
    industry_df : pd.DataFrame
        Output from compute_industry_distribution.
    country_name : str
        Name of the country for titles.
    """
    plt.figure(figsize=(12, 6))

    bars = plt.bar(
        industry_df["Industry"],
        industry_df["Count"],
        width=0.7
    )

    plt.ylim(0, industry_df["Count"].max() * 1.25)
    plt.title(
        f"Number of Billionaires by Industry in {country_name}",
        fontsize=16
    )
    plt.xlabel("Industry", fontsize=14)
    plt.ylabel("Number of Billionaires", fontsize=14)

    for bar, count, perc in zip(
        bars,
        industry_df["Count"],
        industry_df["Percentage"]
    ):
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            yval + 2,
            f"{count}",
            ha="center",
            va="bottom",
            fontsize=11
        )
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            yval / 2,
            f"{perc}%",
            ha="center",
            va="center",
            fontsize=11
        )

    plt.xticks(rotation=65)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    st.pyplot(plt)

# --- Render Total Net Worth By Industry Barplot
def plot_total_net_worth_by_industry(
    df_industry: pd.DataFrame,
    country: str
):
    fig, ax = plt.subplots(figsize=(12, 8))

    bars = ax.bar(
        df_industry["Industry"],
        df_industry["Total net worth"],
        color="teal"
    )

    for bar, value in zip(bars, df_industry["Total net worth"]):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            f"{value}B",
            ha="center",
            va="bottom",
            fontsize=10
        )

    for bar, pct in zip(bars, df_industry["Percentage"]):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() / 2,
            f"{pct}%",
            ha="center",
            va="center",
            fontsize=10,
            color="white"
        )

    ax.set_title(
        f"Billionaires Total Net Worth by Industry in {country} (USD Billion)",
        fontsize=14
    )
    ax.set_xlabel("Industry")
    ax.set_ylabel("Net Worth (USD billion)")
    ax.set_ylim(0, df_industry["Total net worth"].max() * 1.15)
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    return fig

# --- Render YTD Income By Industry Barplot
def plot_ytd_income_by_industry(
    df_industry: pd.DataFrame,
    country: str
):
    fig, ax = plt.subplots(figsize=(16, 8))

    colors = [
        "green" if val >= 0 else "red"
        for val in df_industry["$ YTD change"]
    ]

    bars = ax.bar(
        df_industry["Industry"],
        df_industry["$ YTD change"],
        color=colors
    )

    y_max = df_industry["$ YTD change"].max()
    offset = 0.02 * abs(y_max) if y_max != 0 else 0.1

    for bar, value, pct in zip(
        bars,
        df_industry["$ YTD change"],
        df_industry["Percentage"]
    ):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + offset,
            f"{value}B",
            ha="center",
            va="bottom",
            fontsize=12
        )
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 4 * offset,
            f"{pct}%",
            ha="center",
            va="bottom",
            fontsize=12
        )

    ax.set_title(
        f"Billionaires YTD Net Income by Industry in {country} (USD billion)",
        fontsize=14
    )
    ax.set_xlabel("Industry")
    ax.set_ylabel("Net revenue (USD billion)")

    y_min = df_industry["$ YTD change"].min()
    ax.set_ylim(
        y_min * 1.2 if y_min < 0 else -1,
        y_max * 1.35 if y_max > 0 else 1
    )

    ax.grid(axis="y", linestyle="--", alpha=0.7)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    return fig

# --- Render corelation heat map for countrys 
def plot_country_correlation(corr_matrix: pd.DataFrame, title: str):
    """
    Plot correlation heatmap.
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        ax=ax
    )
    ax.set_title(title)

    return fig

# --- Render Total net worth vs YTD change colored by Industry
def plot_scatter_country(df_scatter: pd.DataFrame, title: str) -> px.scatter:
    """
    Create a scatter plot: Total net worth vs YTD change colored by Industry.
    """
    fig = px.scatter(
        df_scatter,
        x='Total net worth',
        y='$ YTD change',
        color='Industry',
        hover_name='Name',
        size='Total net worth',
        trendline='ols',
        labels={
            'Total net worth': 'Net Worth (USD)',
            '$ YTD change': 'Annual Change (USD)'
        },
        title=title,
        height=800,
        width=1100
    )

    # Ukryj wszystkie branże poza Technology
    for trace in fig.data:
        if trace.name != 'Technology':
            trace.visible = 'legendonly'

    fig.update_layout(
        xaxis_title='Net Worth (USD)',
        yaxis_title='Annual Change (USD)',
        legend_title='Industry',
        template='plotly_white'
    )

    return fig


import matplotlib.pyplot as plt
# --- Render billionaires per industry for a given country.
def plot_industry_barplot_country(counts: pd.Series, percentage: pd.Series, country: str) -> plt.Figure:
    """
    Build barplot of billionaires per industry for a given country.
    
    Parameters
    ----------
    counts : pd.Series
        Number of billionaires per industry.
    percentage : pd.Series
        Percentage of billionaires per industry.
    country : str
        Country name for title.
    
    Returns
    -------
    plt.Figure
        Matplotlib figure object ready to render.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    bars = counts.plot(kind='bar', color='skyblue', width=0.7, ax=ax)

    ax.set_title(f'Number of Billionaires per Industry in {country}', fontsize=16)
    ax.set_xlabel('Industry', fontsize=14)
    ax.set_ylabel('Number of Billionaires', fontsize=14)
    ax.set_ylim(0, counts.max() + 5)

    # Add counts and percentages
    for bar, count, pct in zip(bars.patches, counts, percentage):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, f'{count}', ha='center', va='bottom')
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height()/2, f'{pct}%', ha='center', va='center', color='white')

    plt.xticks(rotation=65)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    return fig

# --- Create a boxplot of total net worth for a single country.
def plot_boxplot_total_net_worth_country(
    df_boxplot: pd.DataFrame,
    country: str
):
    """
    Create a boxplot of total net worth for a single country.

    Parameters
    ----------
    df_boxplot : pd.DataFrame
        Prepared DataFrame containing total net worth values.
    country : str
        Country name used in the plot title.

    Returns
    -------
    plotly.graph_objects.Figure
        Plotly figure ready for rendering.
    """
    fig = px.box(
        df_boxplot,
        x="Total net worth",
        title=f"Boxplot of Total Billionaire Net Worth – {country}",
        labels={
            "Total net worth": "Total Net Worth of the estate (USD)"
        },
        height=800,
        width=1200
    )

    fig.update_layout(
        xaxis_title="Total Net Worth of the estate (USD)",
        template="plotly_white"
    )

    return fig

# --- Create a boxplot of total net worth by industry for a single country.
def plot_industry_boxplot_total_net_worth_country(
    df_boxplot: pd.DataFrame,
    country: str,
    highlight_industry: str = "Technology"
):
    """
    Create a boxplot of total net worth by industry for a single country.

    Parameters
    ----------
    df_boxplot : pd.DataFrame
        Prepared DataFrame with value and industry columns.
    country : str
        Country name used in the plot title.
    highlight_industry : str, optional
        Industry to show by default; others are hidden in legend.

    Returns
    -------
    plotly.graph_objects.Figure
        Plotly figure ready for rendering.
    """
    fig = px.box(
        df_boxplot,
        x="Total net worth",
        y="Industry",
        color="Industry",
        title=f"Boxplot of Total Net Worth by Industry – {country}",
        labels={
            "Total net worth": "Total Net Worth (USD)",
            "Industry": "Industry"
        },
        height=800,
        width=1200
    )

    # Hide all industries except highlighted one
    for trace in fig.data:
        if trace.name != highlight_industry:
            trace.visible = "legendonly"

    fig.update_layout(
        boxmode="group",
        xaxis_title="Total Net Worth (USD)",
        yaxis_title="Industry",
        template="plotly_white"
    )

    return fig

# --- Create a boxplot of last net worth change by industry for a single country.
def plot_industry_boxplot_last_change_country(
    df_boxplot: pd.DataFrame,
    country: str,
    highlight_industry: str = "Technology"
):
    """
    Create a boxplot of last net worth change by industry for a single country.

    Parameters
    ----------
    df_boxplot : pd.DataFrame
        Prepared DataFrame containing last change and industry columns.
    country : str
        Country name used in the plot title.
    highlight_industry : str, optional
        Industry shown by default; others hidden in legend.

    Returns
    -------
    plotly.graph_objects.Figure
        Plotly figure ready for rendering.
    """
    fig = px.box(
        df_boxplot,
        x="$ Last change",
        y="Industry",
        color="Industry",
        title=f"Boxplot of Last Net Worth Change by Industry – {country}",
        labels={
            "$ Last change": "Last Change (USD)",
            "Industry": "Industry"
        },
        height=800,
        width=1100
    )

    for trace in fig.data:
        if trace.name != highlight_industry:
            trace.visible = "legendonly"

    fig.update_layout(
        boxmode="group",
        xaxis_title="Last Change (USD)",
        yaxis_title="Industry",
        template="plotly_white"
    )

    return fig

# --- Plot for Total net worth
def plot_net_worth_histogram_country(
    net_worth: pd.Series,
    country: str,
    bins: int = 80
):
    """
    Plot histogram of total net worth for a single country.

    Parameters
    ----------
    net_worth : pd.Series
        Net worth values.
    country : str
        Country name (used in title).
    bins : int, default 80
        Number of histogram bins.

    Returns
    -------
    matplotlib.figure.Figure
        Histogram figure.
    """
    fig, ax = plt.subplots(figsize=(14, 8))

    sns.histplot(
        net_worth,
        bins=bins,
        kde=True,
        ax=ax
    )

    ax.set_title(f"Distribution of Total Net Worth – {country}")
    ax.set_xlabel("Total Net Worth (USD)")
    ax.set_ylabel("Number of Billionaires")

    plt.tight_layout()
    return fig