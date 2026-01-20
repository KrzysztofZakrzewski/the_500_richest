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
