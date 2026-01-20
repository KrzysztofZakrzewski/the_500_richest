import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go  # !!! Carfull

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

# --- Render Total Net Worth B Industry Barplot
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
