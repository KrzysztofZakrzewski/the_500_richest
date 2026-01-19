import streamlit as st
import pandas as pd

def render_countries(df: pd.DataFrame) -> None:
    st.title("Countries")

    countries = {
        "USA": "United States",
        "China": "China",
        "India": "India",
        "Russia": "Russia",
        "Germany": "Germany",
    }

    tabs = st.tabs(countries.keys())

    for tab, country_name in zip(tabs, countries.values()):
        with tab:
            render_country_view(df, country_name)



def render_country_view(df: pd.DataFrame, country: str) -> None:
    st.markdown(
        f"<h3>General Overview of the Data for {country}</h3>",
        unsafe_allow_html=True
    )

    df_country = df[df["Country / Region"] == country]

    if df_country.empty:
        st.warning("No data available.")
        return

    st.dataframe(df_country)