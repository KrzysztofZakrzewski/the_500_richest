import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go  # !!! Carfull

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


def industry_net_worth_barplot(
    df: pd.DataFrame
) -> plt.Figure:
    """
    Create a bar plot showing total net worth by industry.

    Bars are annotated with net worth values (USD billions) and
    percentage share.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing 'Industry', 'Total net worth' and 'Percentage'.

    Returns
    -------
    matplotlib.figure.Figure
        Matplotlib figure object.
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.bar(df["Industry"], df["Total net worth"], color="teal")

    for bar, value in zip(bars, df["Total net worth"]):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            f"{value}B",
            ha="center",
            va="bottom",
            fontsize=10
        )

    for bar, pct in zip(bars, df["Percentage"]):
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
        "Billionaires Total Net Worth by Industry (USD Billion)",
        fontsize=14
    )
    ax.set_xlabel("Industry")
    ax.set_ylabel("Net Worth (USD billion)")

    ax.set_ylim(
        0,
        df["Total net worth"].max() * 1.15
        if df["Total net worth"].max() > 0 else 1
    )

    plt.xticks(rotation=45, ha="right")
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()

    return fig


def ytd_net_income_barplot(df: pd.DataFrame) -> plt.Figure:
    """
    Create a bar plot for YTD net income by industry.

    Bars are colored green for positive values and red for negative,
    annotated with value (in billions) and percentage.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing 'Industry', '$ YTD change', and 'Percentage'.

    Returns
    -------
    matplotlib.figure.Figure
        Matplotlib figure object.
    """
    fig, ax = plt.subplots(figsize=(16, 8))
    
    # Color bars based on positive/negative
    colors = ['green' if val >= 0 else 'red' for val in df['$ YTD change']]
    bars = ax.bar(df['Industry'], df['$ YTD change'], color=colors)
    
    # Annotate bars
    y_min, y_max = df['$ YTD change'].min(), df['$ YTD change'].max()
    offset = 0.02 * (y_max - y_min if y_max != y_min else 1)
    
    for bar, value, pct in zip(bars, df['$ YTD change'], df['Percentage']):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2,
            height + offset,
            f'{value}B',
            ha='center',
            va='bottom',
            fontsize=12
        )
        ax.text(
            bar.get_x() + bar.get_width()/2,
            height + 4*offset,
            f'{pct}%',
            ha='center',
            va='bottom',
            fontsize=12
        )
    
    # Formatting
    plt.xticks(rotation=45, ha='right')
    ax.set_title('Billionaires YTD Net Income by Industry (USD billion)', fontsize=14)
    ax.set_xlabel('Industry')
    ax.set_ylabel('Net revenue (in billion USD)')
    ax.set_ylim(
        y_min * 1.2 if y_min < 0 else -1,
        y_max * 1.35 if y_max > 0 else 1
    )
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.subplots_adjust(right=0.95, left=0.1, top=0.9, bottom=0.25)
    plt.tight_layout()
    
    return fig


def coutry_plot_correlation_matrix(correlation_matrix: pd.DataFrame) -> plt.Figure:
    """
    Create a heatmap plot of a correlation matrix.

    Parameters
    ----------
    correlation_matrix : pd.DataFrame
        DataFrame containing correlation values.

    Returns
    -------
    matplotlib.figure.Figure
        Matplotlib figure object ready for rendering.
    """
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    ax.set_title('Correlation Matrix')
    plt.tight_layout()
    return fig


import plotly.express as px

def plot_growth_vs_assets(df: pd.DataFrame) -> go.Figure:
    """
    Create a scatter plot of Total net worth vs YTD change, colored by Industry,
    with trendline for Technology and others initially hidden.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing 'Total net worth', '$ YTD change', 'Industry', 'Name'.

    Returns
    -------
    plotly.graph_objects.Figure
        Plotly scatter figure.
    """
    fig = px.scatter(
        df,
        x='Total net worth',
        y='$ YTD change',
        color='Industry',
        hover_name='Name',
        size='Total net worth',
        trendline='ols',
        labels={
            'Total net worth': 'Majątek netto (USD)',
            '$ YTD change': 'Roczna zmiana (USD)'
        },
        title='Growth in income relative to assets for various industries',
        height=800,
        width=1100
    )
    
    # Ukryj wszystkie branże poza Technology
    for trace in fig.data:
        if trace.name != 'Technology':
            trace.visible = 'legendonly'
    
    fig.update_layout(
        xaxis_title='Net worth (USD)',
        yaxis_title='Annual change (USD)',
        legend_title='Industry',
        template='plotly_white'
    )
    
    return fig

# ===========
# OUTLINERS

def plot_total_net_worth_box(df: pd.DataFrame) -> go.Figure:
    """
    Create a boxplot of total net worth for all billionaires.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing 'Total net worth'.

    Returns
    -------
    plotly.graph_objects.Figure
        Plotly boxplot figure.
    """
    fig = px.box(
        df,
        x='Total net worth',
        title='Boxplot of Total Billionaire Net Worth of the estate',
        labels={'Total net worth': 'Total Net Worth of the estate (USD)'},
        height=800,
        width=1200
    )
    
    fig.update_layout(
        xaxis_title='Total Net Worth of the estate (USD)',
        template='plotly_white'
    )
    
    return fig

# def plot_net_worth_by_industry_box(df: pd.DataFrame, highlight_industry: str = 'Technology') -> go.Figure:
#     """
#     Create a grouped boxplot of total net worth by industry.

#     Optionally, highlight one industry (others hidden by default).

#     Parameters
#     ----------
#     df : pd.DataFrame
#         DataFrame containing 'Total net worth' and 'Industry'.
#     highlight_industry : str, optional
#         Industry to highlight (default 'Technology').

#     Returns
#     -------
#     plotly.graph_objects.Figure
#         Plotly boxplot figure grouped by Industry.
#     """
#     fig = px.box(
#         df,
#         x='Total net worth',
#         y='Industry',
#         color='Industry',
#         title='Total Net Worth of Billionaires by Industry',
#         labels={
#             'Total net worth': 'Total net worth (USD)',
#             'Industry': 'Industry'
#         },
#         height=800,
#         width=1200
#     )

#     # Ukryj wszystkie branże poza highlight_industry
#     for trace in fig.data:
#         if trace.name != highlight_industry:
#             trace.visible = 'legendonly'

#     fig.update_layout(
#         boxmode='group',
#         xaxis_title='Total net worth (USD)',
#         yaxis_title='Industry',
#         template='plotly_white'
#     )

#     return fig



def universal_plot_box_by_industry(
    df: pd.DataFrame,
    x_col: str,
    title: str,
    x_label: str,
    highlight_industry: str = 'Technology',
    height: int = 800,
    width: int = 1200
) -> go.Figure:
    """
    Create a grouped boxplot of a numeric column by Industry.

    Optionally, highlight one industry (others hidden by default).

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the columns to plot.
    x_col : str
        Column name to plot on X axis.
    title : str
        Plot title.
    x_label : str
        Label for X axis.
    highlight_industry : str, optional
        Industry to highlight (default 'Technology').
    height : int, optional
        Plot height (default 800).
    width : int, optional
        Plot width (default 1200).

    Returns
    -------
    plotly.graph_objects.Figure
    """
    fig = px.box(
        df,
        x=x_col,
        y='Industry',
        color='Industry',
        title=title,
        labels={x_col: x_label, 'Industry': 'Industry'},
        height=height,
        width=width
    )

    # Hide all traces except highlight_industry
    for trace in fig.data:
        if trace.name != highlight_industry:
            trace.visible = 'legendonly'

    fig.update_layout(
        boxmode='group',
        xaxis_title=x_label,
        yaxis_title='Industry',
        template='plotly_white'
    )

    return fig
