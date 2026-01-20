#==============
# IMPORTS
#==============

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import statsmodels.api as sm
import io
#==============
# --- Inner Imports
#==============
# --- Global
from loader.csv_loader import (load_data)
from ui.styles import (inject_global_css)
from ui.sidebar import (render_sidebar)
from ui.pages.about import (render_about)
from ui.pages.global_analis import (render_global_analysis)

# --- Countrys
from ui.pages.countrys import (render_countries)

# --- Set global float display format for better readability
pd.options.display.float_format = '{:,.2f}'.format

# --- Web set
st.set_page_config(
    page_title="Krzysztof Zakrzeski",
    layout="wide")

inject_global_css()

col1, col2, col3 = st.columns([1, 4, 1])

# =============
# LOAD DATAFRAME
# =============

df_ready = load_data(path='top_rich2024_ready.csv')

# =============
# UI
# =============

section = render_sidebar()
with col2:

    # =============
    # Render UI
    # =============

    if section == "About":
        render_about()
    elif section == "Global analysis":
        render_global_analysis(df_ready)
    elif section == "Countrys":
        render_countries(df_ready)