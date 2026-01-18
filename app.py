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

# --- Inner Imports
from loader.csv_loader import (load_data)
from ui.styles import (inject_global_css)
from ui.sidebar import (render_sidebar)
from ui.pages.about import (render_about)
from ui.pages.global_analis import (render_global_analysis)


# --- Set global float display format for better readability
pd.options.display.float_format = '{:,.2f}'.format

# --- Web set
st.set_page_config(
    page_title="My App",
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

    # if content_section == 'Countrys':
    #     st.title('Countrys')
    #     tab0, tab1, tab2, tab3, tab4 = st.tabs(["USA", "China", "India", "Rusia", "Germany"])
    #     with tab0:
    #         st.markdown('<h3 ># STEP 1: General Overview of the Data for USA</h3>', unsafe_allow_html=True)
    #         # st.write(df_ready['Country / Region'].unique())
    #         df_usa = df_ready[df_ready['Country / Region'] == 'United States'].copy()
    #         df_usa

    #         # RESET INDEX

    #         buffer_usa = io.StringIO()
    #         df_usa.info(buf=buffer_usa)
    #         info_str_usa = buffer_usa.getvalue()

    #         ############
    #         # STEP 1
    #         # 

    #         # df_usa.info w Streamlit
    #         st.markdown('<h4>Basic information:</h4>', unsafe_allow_html=True)
    #         st.text(info_str_usa)

    #         st.markdown('<h4>Nunique values</h4>', unsafe_allow_html=True)
    #         st.write(df_usa.nunique())

    #         st.write(f'Unique values in total: {df_usa.nunique().sum()}')
    #         st.markdown('<h4>Descritive Statistics</h4>', unsafe_allow_html=True)
    #         st.write(df_usa.describe().T)

    #         st.markdown('<h3 ># STEP 2: Single Variable Analysis</h3>', unsafe_allow_html=True)
    #         st.markdown('<h4>Barplot for Bilioners in each industry in USA</h4>', unsafe_allow_html=True)


    #         industry_counts = df_usa['Industry'].value_counts()
    #         total_records = len(df_usa)
    #         percentage = (industry_counts / total_records) * 100

    #         plt.figure(figsize=(12, 6))
    #         bars = industry_counts.plot(kind='bar', color='skyblue', width=0.7)

    #         plt.ylim(0, industry_counts.max() + 20)
    #         plt.title('Number of Bilioners in each industry in usa', fontsize=16)
    #         plt.xlabel('Industry', fontsize=14)
    #         plt.ylabel('Number of Bilioners', fontsize=14)

    #         for bar, count, perc in zip(bars.patches, industry_counts, percentage):
    #             yval = bar.get_height()
    #             plt.text(bar.get_x() + bar.get_width()/2, yval + 5, f'{count}', ha='center', va='bottom', fontsize=12)
    #             plt.text(bar.get_x() + bar.get_width()/2, yval/2, f'{perc:.1f}%', ha='center', va='center', fontsize=12)

    #         plt.xticks(rotation=65, fontsize=12)
    #         plt.yticks(fontsize=12)
    #         plt.grid(axis='y', linestyle='--', alpha=0.7)
    #         plt.tight_layout()
    #         st.pyplot(plt)

    #         st.markdown('<h4>Barplot for Billionaires Total Net Worth by Industry in USA (USD Billion)</h4>', unsafe_allow_html=True)

    #         total_net_worth_ind_usa_df = df_usa.groupby('Industry', as_index=False)['Total net worth'].sum()
    #         total_net_worth_ind_usa_df = total_net_worth_ind_usa_df.sort_values(by='Total net worth', ascending=False).reset_index(drop=True)
    #         total_net_worth_ind_usa_df['Total net worth'] = (total_net_worth_ind_usa_df['Total net worth'] / 1e9).round(1)
    #         total_net_worth_ind_usa_df['Percentage'] = (total_net_worth_ind_usa_df['Total net worth'] / total_net_worth_ind_usa_df['Total net worth'].sum() * 100).round(1)
    #         plt.figure(figsize=(12, 8))
    #         bars = plt.bar(total_net_worth_ind_usa_df['Industry'], total_net_worth_ind_usa_df['Total net worth'], color='teal')
    #         for bar, value in zip(bars, total_net_worth_ind_usa_df['Total net worth']):
    #             plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f'{value}B', 
    #                     ha='center', va='bottom', fontsize=10)
    #         for bar, pct in zip(bars, total_net_worth_ind_usa_df['Percentage']):
    #             plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, f'{pct}%', 
    #                     ha='center', va='center', fontsize=10, color='white')
    #         plt.xticks(rotation=45, ha='right')
    #         plt.title('Billionaires Total Net Worth by Industry in USA (USD Billion)', fontsize=14)
    #         plt.xlabel('Industry')
    #         plt.ylabel('Net Worth (in USD billion)')
    #         y_max = total_net_worth_ind_usa_df['Total net worth'].max()
    #         plt.ylim(0, y_max * 1.15 if y_max > 0 else 1)
    #         plt.grid(axis='y', linestyle='--', alpha=0.7)
    #         plt.tight_layout()
    #         st.pyplot(plt)

    #         st.markdown('<h4>YTD net income of Millionaires in a given industry in USA</h4>', unsafe_allow_html=True)

    #         ytd_net_income_ind_usa_df = df_usa.groupby('Industry', as_index=False)['$ YTD change'].sum()
    #         ytd_net_income_ind_usa_df = ytd_net_income_ind_usa_df.sort_values(by='$ YTD change', ascending=False).reset_index(drop=True)
    #         ytd_net_income_ind_usa_df['$ YTD change'] = pd.to_numeric(ytd_net_income_ind_usa_df['$ YTD change'], errors='coerce').fillna(0)
    #         ytd_net_income_ind_usa_df['$ YTD change'] = (ytd_net_income_ind_usa_df['$ YTD change'] / 1e9).round(2)
    #         total_sum = ytd_net_income_ind_usa_df['$ YTD change'].sum()
    #         ytd_net_income_ind_usa_df['Percentage'] = (ytd_net_income_ind_usa_df['$ YTD change'] / total_sum * 100).round(1)
    #         plt.figure(figsize=(16, 8))
    #         bars = plt.bar(
    #             ytd_net_income_ind_usa_df['Industry'], 
    #             ytd_net_income_ind_usa_df['$ YTD change'], 
    #             color=['green' if val >= 0 else 'red' for val in ytd_net_income_ind_usa_df['$ YTD change']]
    #         )
    #         for bar, value, pct in zip(bars, ytd_net_income_ind_usa_df['$ YTD change'], ytd_net_income_ind_usa_df['Percentage']):
    #             height = bar.get_height()
    #             offset = 0.02 * plt.ylim()[1]
    #             plt.text(
    #                 bar.get_x() + bar.get_width() / 2, 
    #                 height + offset, 
    #                 f'{value}B', 
    #                 ha='center', va='bottom', fontsize=12
    #             )
    #             plt.text(
    #                 bar.get_x() + bar.get_width() / 2, 
    #                 height + 4 * offset, 
    #                 f'{pct}%', 
    #                 ha='center', va='bottom', fontsize=12
    #             )
    #         plt.xticks(rotation=45, ha='right')
    #         plt.title('Billionaires YTD Net Income by Industry (USD billion)', fontsize=14)
    #         plt.xlabel('Industry')
    #         plt.ylabel('Net revenue (in billion USD)')
    #         y_min = ytd_net_income_ind_usa_df['$ YTD change'].min()
    #         y_max = ytd_net_income_ind_usa_df['$ YTD change'].max()
    #         plt.ylim(
    #             y_min * 1.2 if y_min < 0 else -1,
    #             y_max * 1.35 if y_max > 0 else 1
    #         )
    #         plt.grid(axis='y', linestyle='--', alpha=0.7)
    #         plt.subplots_adjust(right=0.95, left=0.1, top=0.9, bottom=0.25)
    #         plt.tight_layout()
    #         st.pyplot(plt)

    #         st.markdown('<h3 ># STEP 3: Correlations</h3>', unsafe_allow_html=True)

    #         st.markdown('<h4>Correlation Matrix for bilioners in USA</h4>', unsafe_allow_html=True)

    #         corr_usa_df = df_usa.copy()
    #         corr_usa_df = corr_usa_df.drop(columns = ['Name', 'Rank', 'Country / Region', 'Industry'])
    #         corr_usa_df.corr()
    #         correlation_matrix_usa = corr_usa_df.corr()

    #         # Tworzenie wykresu macierzy korelacji
    #         plt.figure(figsize=(10, 8))
    #         sns.heatmap(correlation_matrix_usa, annot=True, cmap='coolwarm', fmt='.2f')
    #         plt.title('Correlation Matrix')
    #         st.pyplot(plt)


    #         st.markdown('<h4>Interactive scaterplot for bilioners in USA</h4>', unsafe_allow_html=True)

    #         df_filtered_usa = df_usa.copy()
    #         fig = px.scatter(
    #             df_filtered_usa,
    #             x='Total net worth',
    #             y='$ YTD change',
    #             color='Industry',
    #             hover_name='Name',
    #             size='Total net worth',
    #             trendline='ols',
    #             labels={
    #                 'Total net worth': 'Net Worth (USD)',
    #                 '$ YTD change': 'Annual Change (USD)'
    #             },
    #             title='Growth in Income Relative to Assets for Various Industries',
    #             height=800,
    #             width=1100
    #         )
    #         for trace in fig.data:
    #             if trace.name != 'Technology':
    #                 trace.visible = 'legendonly'
    #         fig.update_layout(
    #             xaxis_title='Net Worth (USD)',
    #             yaxis_title='Annual Change (USD)',
    #             legend_title='Industry',
    #             template='plotly_white'
    #         )
    #         st.plotly_chart(fig, use_container_width=True)


    #         # # # # # # # #
    #         # STEP 4

    #         st.markdown('<h3 ># STEP 4: Outlier Analysis for USA</h3>', unsafe_allow_html=True)

    #         st.markdown('<h4 >Boxplot of Total Net Worth of Billionaires in USA</h4>', unsafe_allow_html=True)

    #         fig = px.box(
    #         df_usa,
    #         x='Total net worth',
    #         title='Boxplot of Total Billionaire Net Worth of the estate',
    #         labels={'Total net worth': 'Total Net Worth of the estate (USD)'},
    #         height=800,
    #         width=1200
    #         )
    #         fig.update_layout(
    #             xaxis_title='Total Net Worth of the estate (USD)',
    #             template='plotly_white'
    #         )
    #         st.plotly_chart(fig, use_container_width=True)


    #         st.markdown('<h4 >Boxplot of Total Net Worth of Billionaires by Industry in USA</h4>', unsafe_allow_html=True)

    #         fig = px.box(
    #             df_usa,
    #             x='Total net worth',
    #             y='Industry',
    #             color='Industry',
    #             title='Boxplot of Total Net Worth of Billionaires by Industry in USA',
    #             labels={
    #                 'Total net worth': 'Total Net Worth (USD)',
    #                 'Industry': 'Industry'
    #             },
    #             height=800,
    #             width=1200
    #         )
    #         for trace in fig.data:
    #             if trace.name != 'Technology':
    #                 trace.visible = 'legendonly'
    #         fig.update_layout(
    #             boxmode='group',
    #             xaxis_title='Total Net Worth (USD)',
    #             yaxis_title='Industry',
    #             template='plotly_white'
    #         )
    #         st.plotly_chart(fig, use_container_width=True)


    #         st.markdown('<h4 >Boxplot of last change net worth ($ Last change) for industries in USA</h4>', unsafe_allow_html=True)

    #         fig = px.box(
    #             df_usa,
    #             x='$ Last change',
    #             y='Industry',
    #             color='Industry',
    #             title='Boxplot of last change net worth ($ Last change) for industries in USA',
    #             labels={
    #                 '$ Last change': 'Last Change (USD)',
    #                 'Industry': 'Industry'
    #             },
    #             height=800,
    #             width=1100
    #         )

    #         for trace in fig.data:
    #             if trace.name != 'Technology':
    #                 trace.visible = 'legendonly'

    #         fig.update_layout(
    #             boxmode='group',
    #             xaxis_title='Last Change (USD)',
    #             yaxis_title='Industry',
    #             template='plotly_white'
    #         )

    #         st.plotly_chart(fig, use_container_width=True)

    #         st.markdown('<h4 >Histogram of the number of bilioners in Usa</h4>', unsafe_allow_html=True)

    #         plt.figure(figsize=(14, 8))
    #         sns.histplot(df_usa['Total net worth'], bins=80, kde=True)  # Możesz dostosować liczbę bins
    #         plt.title('Histogram of the number of bilioners in Usa')
    #         plt.xlabel('Total Net Worth')
    #         plt.ylabel('Number of occurrences')
    #         st.pyplot(plt)

    #     with tab1:
    #         st.markdown('<h3 ># STEP 1: General Overview of the Data for China</h3>', unsafe_allow_html=True)
    #         # st.write(df_ready['Country / Region'].unique())
    #         df_china = df_ready[df_ready['Country / Region'] == 'China'].copy()
    #         df_china

    #         # RESET INDEX

    #         buffer_china = io.StringIO()
    #         df_china.info(buf=buffer_china)
    #         info_str_china = buffer_china.getvalue()

    #         ############
    #         # STEP 1
    #         # 

    #         # df_china.info w Streamlit
    #         st.markdown('<h4>Basic information:</h4>', unsafe_allow_html=True)
    #         st.text(info_str_china)

    #         st.markdown('<h4>Nunique values</h4>', unsafe_allow_html=True)
    #         st.write(df_china.nunique())

    #         st.write(f'Unique values in total: {df_china.nunique().sum()}')
    #         st.markdown('<h4>Descritive Statistics</h4>', unsafe_allow_html=True)
    #         st.write(df_china.describe().T)

    #         st.markdown('<h3 ># STEP 2: Single Variable Analysis</h3>', unsafe_allow_html=True)
    #         st.markdown('<h4>Barplot for Bilioners in each industry in China</h4>', unsafe_allow_html=True)


    #         industry_counts = df_china['Industry'].value_counts()
    #         total_records = len(df_china)
    #         percentage = (industry_counts / total_records) * 100

    #         plt.figure(figsize=(12, 6))
    #         bars = industry_counts.plot(kind='bar', color='skyblue', width=0.7)

    #         plt.ylim(0, industry_counts.max() + 20)
    #         plt.title('Number of Bilioners in each industry in China', fontsize=16)
    #         plt.xlabel('Industry', fontsize=14)
    #         plt.ylabel('Number of Bilioners', fontsize=14)

    #         for bar, count, perc in zip(bars.patches, industry_counts, percentage):
    #             yval = bar.get_height()
    #             plt.text(bar.get_x() + bar.get_width()/2, yval + 5, f'{count}', ha='center', va='bottom', fontsize=12)
    #             plt.text(bar.get_x() + bar.get_width()/2, yval/2, f'{perc:.1f}%', ha='center', va='center', fontsize=12)

    #         plt.xticks(rotation=65, fontsize=12)
    #         plt.yticks(fontsize=12)
    #         plt.grid(axis='y', linestyle='--', alpha=0.7)
    #         plt.tight_layout()
    #         st.pyplot(plt)

    #         st.markdown('<h4>Barplot for Billionaires Total Net Worth by Industry in China (USD Billion)</h4>', unsafe_allow_html=True)

    #         total_net_worth_ind_china_df = df_china.groupby('Industry', as_index=False)['Total net worth'].sum()
    #         total_net_worth_ind_china_df = total_net_worth_ind_china_df.sort_values(by='Total net worth', ascending=False).reset_index(drop=True)
    #         total_net_worth_ind_china_df['Total net worth'] = (total_net_worth_ind_china_df['Total net worth'] / 1e9).round(1)
    #         total_net_worth_ind_china_df['Percentage'] = (total_net_worth_ind_china_df['Total net worth'] / total_net_worth_ind_china_df['Total net worth'].sum() * 100).round(1)
    #         plt.figure(figsize=(12, 8))
    #         bars = plt.bar(total_net_worth_ind_china_df['Industry'], total_net_worth_ind_china_df['Total net worth'], color='teal')
    #         for bar, value in zip(bars, total_net_worth_ind_china_df['Total net worth']):
    #             plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f'{value}B', 
    #                     ha='center', va='bottom', fontsize=10)
    #         for bar, pct in zip(bars, total_net_worth_ind_china_df['Percentage']):
    #             plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, f'{pct}%', 
    #                     ha='center', va='center', fontsize=10, color='white')
    #         plt.xticks(rotation=45, ha='right')
    #         plt.title('Billionaires Total Net Worth by Industry in China (USD Billion)', fontsize=14)
    #         plt.xlabel('Industry')
    #         plt.ylabel('Net Worth (in USD billion)')
    #         y_max = total_net_worth_ind_china_df['Total net worth'].max()
    #         plt.ylim(0, y_max * 1.15 if y_max > 0 else 1)
    #         plt.grid(axis='y', linestyle='--', alpha=0.7)
    #         plt.tight_layout()
    #         st.pyplot(plt)

    #         st.markdown('<h4>YTD net income of Millionaires in a given industry in China</h4>', unsafe_allow_html=True)

    #         ytd_net_income_ind_china_df = df_china.groupby('Industry', as_index=False)['$ YTD change'].sum()
    #         ytd_net_income_ind_china_df = ytd_net_income_ind_china_df.sort_values(by='$ YTD change', ascending=False).reset_index(drop=True)
    #         ytd_net_income_ind_china_df['$ YTD change'] = pd.to_numeric(ytd_net_income_ind_china_df['$ YTD change'], errors='coerce').fillna(0)
    #         ytd_net_income_ind_china_df['$ YTD change'] = (ytd_net_income_ind_china_df['$ YTD change'] / 1e9).round(2)
    #         total_sum = ytd_net_income_ind_china_df['$ YTD change'].sum()
    #         ytd_net_income_ind_china_df['Percentage'] = (ytd_net_income_ind_china_df['$ YTD change'] / total_sum * 100).round(1)
    #         plt.figure(figsize=(16, 8))
    #         bars = plt.bar(
    #             ytd_net_income_ind_china_df['Industry'], 
    #             ytd_net_income_ind_china_df['$ YTD change'], 
    #             color=['green' if val >= 0 else 'red' for val in ytd_net_income_ind_china_df['$ YTD change']]
    #         )
    #         for bar, value, pct in zip(bars, ytd_net_income_ind_china_df['$ YTD change'], ytd_net_income_ind_china_df['Percentage']):
    #             height = bar.get_height()
    #             offset = 0.02 * plt.ylim()[1]
    #             plt.text(
    #                 bar.get_x() + bar.get_width() / 2, 
    #                 height + offset, 
    #                 f'{value}B', 
    #                 ha='center', va='bottom', fontsize=12
    #             )
    #             plt.text(
    #                 bar.get_x() + bar.get_width() / 2, 
    #                 height + 4 * offset, 
    #                 f'{pct}%', 
    #                 ha='center', va='bottom', fontsize=12
    #             )
    #         plt.xticks(rotation=45, ha='right')
    #         plt.title('Billionaires YTD Net Income by Industry (USD billion)', fontsize=14)
    #         plt.xlabel('Industry')
    #         plt.ylabel('Net revenue (in billion USD)')
    #         y_min = ytd_net_income_ind_china_df['$ YTD change'].min()
    #         y_max = ytd_net_income_ind_china_df['$ YTD change'].max()
    #         plt.ylim(
    #             y_min * 1.2 if y_min < 0 else -1,
    #             y_max * 1.35 if y_max > 0 else 1
    #         )
    #         plt.grid(axis='y', linestyle='--', alpha=0.7)
    #         plt.subplots_adjust(right=0.95, left=0.1, top=0.9, bottom=0.25)
    #         plt.tight_layout()
    #         st.pyplot(plt)

    #         st.markdown('<h3 ># STEP 3: Correlations</h3>', unsafe_allow_html=True)

    #         st.markdown('<h4>Correlation Matrix for bilioners in China</h4>', unsafe_allow_html=True)

    #         corr_china_df = df_china.copy()
    #         corr_china_df = corr_china_df.drop(columns = ['Name', 'Rank', 'Country / Region', 'Industry'])
    #         corr_china_df.corr()
    #         correlation_matrix_china = corr_china_df.corr()

    #         # Tworzenie wykresu macierzy korelacji
    #         plt.figure(figsize=(10, 8))
    #         sns.heatmap(correlation_matrix_china, annot=True, cmap='coolwarm', fmt='.2f')
    #         plt.title('Correlation Matrix')
    #         st.pyplot(plt)


    #         st.markdown('<h4>Interactive scaterplot for bilioners in China</h4>', unsafe_allow_html=True)

    #         df_filtered_china = df_china.copy()
    #         fig = px.scatter(
    #             df_filtered_china,
    #             x='Total net worth',
    #             y='$ YTD change',
    #             color='Industry',
    #             hover_name='Name',
    #             size='Total net worth',
    #             trendline='ols',
    #             labels={
    #                 'Total net worth': 'Net Worth (USD)',
    #                 '$ YTD change': 'Annual Change (USD)'
    #             },
    #             title='Growth in Income Relative to Assets for Various Industries',
    #             height=800,
    #             width=1100
    #         )
    #         for trace in fig.data:
    #             if trace.name != 'Technology':
    #                 trace.visible = 'legendonly'
    #         fig.update_layout(
    #             xaxis_title='Net Worth (USD)',
    #             yaxis_title='Annual Change (USD)',
    #             legend_title='Industry',
    #             template='plotly_white'
    #         )
    #         st.plotly_chart(fig, use_container_width=True)


    #         # # # # # # # #
    #         # STEP 4

    #         st.markdown('<h3 ># STEP 4: Outlier Analysis for China</h3>', unsafe_allow_html=True)

    #         st.markdown('<h4 >Boxplot of Total Net Worth of Billionaires in China</h4>', unsafe_allow_html=True)

    #         fig = px.box(
    #         df_china,
    #         x='Total net worth',
    #         title='Boxplot of Total Billionaire Net Worth of the estate',
    #         labels={'Total net worth': 'Total Net Worth of the estate (USD)'},
    #         height=800,
    #         width=1200
    #         )
    #         fig.update_layout(
    #             xaxis_title='Total Net Worth of the estate (USD)',
    #             template='plotly_white'
    #         )
    #         st.plotly_chart(fig, use_container_width=True)


    #         st.markdown('<h4 >Boxplot of Total Net Worth of Billionaires by Industry in China</h4>', unsafe_allow_html=True)

    #         fig = px.box(
    #             df_china,
    #             x='Total net worth',
    #             y='Industry',
    #             color='Industry',
    #             title='Boxplot of Total Net Worth of Billionaires by Industry in China',
    #             labels={
    #                 'Total net worth': 'Total Net Worth (USD)',
    #                 'Industry': 'Industry'
    #             },
    #             height=800,
    #             width=1200
    #         )
    #         for trace in fig.data:
    #             if trace.name != 'Technology':
    #                 trace.visible = 'legendonly'
    #         fig.update_layout(
    #             boxmode='group',
    #             xaxis_title='Total Net Worth (USD)',
    #             yaxis_title='Industry',
    #             template='plotly_white'
    #         )
    #         st.plotly_chart(fig, use_container_width=True)


    #         st.markdown('<h4 >Boxplot of last change net worth ($ Last change) for industries in China</h4>', unsafe_allow_html=True)

    #         fig = px.box(
    #             df_china,
    #             x='$ Last change',
    #             y='Industry',
    #             color='Industry',
    #             title='Boxplot of last change net worth ($ Last change) for industries in China',
    #             labels={
    #                 '$ Last change': 'Last Change (USD)',
    #                 'Industry': 'Industry'
    #             },
    #             height=800,
    #             width=1100
    #         )

    #         for trace in fig.data:
    #             if trace.name != 'Technology':
    #                 trace.visible = 'legendonly'

    #         fig.update_layout(
    #             boxmode='group',
    #             xaxis_title='Last Change (USD)',
    #             yaxis_title='Industry',
    #             template='plotly_white'
    #         )

    #         st.plotly_chart(fig, use_container_width=True)

    #         st.markdown('<h4 >Histogram of the number of bilioners of df China</h4>', unsafe_allow_html=True)

    #         plt.figure(figsize=(14, 8))
    #         sns.histplot(df_china['Total net worth'], bins=80, kde=True)
    #         plt.title('Histogram of the number of bilioners of df China')
    #         plt.xlabel('Total Net Worth')
    #         plt.ylabel('Number of occurrences')
    #         st.pyplot(plt)

    #     with tab2:
    #         st.markdown('<h3 ># STEP 1: General Overview of the Data for India</h3>', unsafe_allow_html=True)
    #         # st.write(df_ready['Country / Region'].unique())
    #         df_india = df_ready[df_ready['Country / Region'] == 'India'].copy()
    #         df_india

    #         # RESET INDEX

    #         buffer_india = io.StringIO()
    #         df_india.info(buf=buffer_india)
    #         info_str_india = buffer_india.getvalue()

    #         ############
    #         # STEP 1
    #         # 

    #         # df_india.info w Streamlit
    #         st.markdown('<h4>Basic information:</h4>', unsafe_allow_html=True)
    #         st.text(info_str_india)

    #         st.markdown('<h4>Nunique values</h4>', unsafe_allow_html=True)
    #         st.write(df_india.nunique())

    #         st.write(f'Unique values in total: {df_india.nunique().sum()}')
    #         st.markdown('<h4>Descritive Statistics</h4>', unsafe_allow_html=True)
    #         st.write(df_india.describe().T)

    #         st.markdown('<h3 ># STEP 2: Single Variable Analysis</h3>', unsafe_allow_html=True)
    #         st.markdown('<h4>Barplot for Bilioners in each industry in India</h4>', unsafe_allow_html=True)


    #         industry_counts = df_india['Industry'].value_counts()
    #         total_records = len(df_india)
    #         percentage = (industry_counts / total_records) * 100

    #         plt.figure(figsize=(12, 6))
    #         bars = industry_counts.plot(kind='bar', color='skyblue', width=0.7)

    #         plt.ylim(0, industry_counts.max() + 20)
    #         plt.title('Number of Bilioners in each industry in India', fontsize=16)
    #         plt.xlabel('Industry', fontsize=14)
    #         plt.ylabel('Number of Bilioners', fontsize=14)

    #         for bar, count, perc in zip(bars.patches, industry_counts, percentage):
    #             yval = bar.get_height()
    #             plt.text(bar.get_x() + bar.get_width()/2, yval + 5, f'{count}', ha='center', va='bottom', fontsize=12)
    #             plt.text(bar.get_x() + bar.get_width()/2, yval/2, f'{perc:.1f}%', ha='center', va='center', fontsize=12)

    #         plt.xticks(rotation=65, fontsize=12)
    #         plt.yticks(fontsize=12)
    #         plt.grid(axis='y', linestyle='--', alpha=0.7)
    #         plt.tight_layout()
    #         st.pyplot(plt)

    #         st.markdown('<h4>Barplot for Billionaires Total Net Worth by Industry in India (USD Billion)</h4>', unsafe_allow_html=True)

    #         total_net_worth_ind_india_df = df_india.groupby('Industry', as_index=False)['Total net worth'].sum()
    #         total_net_worth_ind_india_df = total_net_worth_ind_india_df.sort_values(by='Total net worth', ascending=False).reset_index(drop=True)
    #         total_net_worth_ind_india_df['Total net worth'] = (total_net_worth_ind_india_df['Total net worth'] / 1e9).round(1)
    #         total_net_worth_ind_india_df['Percentage'] = (total_net_worth_ind_india_df['Total net worth'] / total_net_worth_ind_india_df['Total net worth'].sum() * 100).round(1)
    #         plt.figure(figsize=(12, 8))
    #         bars = plt.bar(total_net_worth_ind_india_df['Industry'], total_net_worth_ind_india_df['Total net worth'], color='teal')
    #         for bar, value in zip(bars, total_net_worth_ind_india_df['Total net worth']):
    #             plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f'{value}B', 
    #                     ha='center', va='bottom', fontsize=10)
    #         for bar, pct in zip(bars, total_net_worth_ind_india_df['Percentage']):
    #             plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, f'{pct}%', 
    #                     ha='center', va='center', fontsize=10, color='white')
    #         plt.xticks(rotation=45, ha='right')
    #         plt.title('Billionaires Total Net Worth by Industry in India (USD Billion)', fontsize=14)
    #         plt.xlabel('Industry')
    #         plt.ylabel('Net Worth (in USD billion)')
    #         y_max = total_net_worth_ind_india_df['Total net worth'].max()
    #         plt.ylim(0, y_max * 1.15 if y_max > 0 else 1)
    #         plt.grid(axis='y', linestyle='--', alpha=0.7)
    #         plt.tight_layout()
    #         st.pyplot(plt)

    #         st.markdown('<h4>YTD net income of Millionaires in a given industry in India</h4>', unsafe_allow_html=True)

    #         ytd_net_income_ind_india_df = df_india.groupby('Industry', as_index=False)['$ YTD change'].sum()
    #         ytd_net_income_ind_india_df = ytd_net_income_ind_india_df.sort_values(by='$ YTD change', ascending=False).reset_index(drop=True)
    #         ytd_net_income_ind_india_df['$ YTD change'] = pd.to_numeric(ytd_net_income_ind_india_df['$ YTD change'], errors='coerce').fillna(0)
    #         ytd_net_income_ind_india_df['$ YTD change'] = (ytd_net_income_ind_india_df['$ YTD change'] / 1e9).round(2)
    #         total_sum = ytd_net_income_ind_india_df['$ YTD change'].sum()
    #         ytd_net_income_ind_india_df['Percentage'] = (ytd_net_income_ind_india_df['$ YTD change'] / total_sum * 100).round(1)
    #         plt.figure(figsize=(16, 8))
    #         bars = plt.bar(
    #             ytd_net_income_ind_india_df['Industry'], 
    #             ytd_net_income_ind_india_df['$ YTD change'], 
    #             color=['green' if val >= 0 else 'red' for val in ytd_net_income_ind_india_df['$ YTD change']]
    #         )
    #         for bar, value, pct in zip(bars, ytd_net_income_ind_india_df['$ YTD change'], ytd_net_income_ind_india_df['Percentage']):
    #             height = bar.get_height()
    #             offset = 0.02 * plt.ylim()[1]
    #             plt.text(
    #                 bar.get_x() + bar.get_width() / 2, 
    #                 height + offset, 
    #                 f'{value}B', 
    #                 ha='center', va='bottom', fontsize=12
    #             )
    #             plt.text(
    #                 bar.get_x() + bar.get_width() / 2, 
    #                 height + 4 * offset, 
    #                 f'{pct}%', 
    #                 ha='center', va='bottom', fontsize=12
    #             )
    #         plt.xticks(rotation=45, ha='right')
    #         plt.title('Billionaires YTD Net Income by Industry (USD billion)', fontsize=14)
    #         plt.xlabel('Industry')
    #         plt.ylabel('Net revenue (in billion USD)')
    #         y_min = ytd_net_income_ind_india_df['$ YTD change'].min()
    #         y_max = ytd_net_income_ind_india_df['$ YTD change'].max()
    #         plt.ylim(
    #             y_min * 1.2 if y_min < 0 else -1,
    #             y_max * 1.35 if y_max > 0 else 1
    #         )
    #         plt.grid(axis='y', linestyle='--', alpha=0.7)
    #         plt.subplots_adjust(right=0.95, left=0.1, top=0.9, bottom=0.25)
    #         plt.tight_layout()
    #         st.pyplot(plt)

    #         st.markdown('<h3 ># STEP 3: Correlations</h3>', unsafe_allow_html=True)

    #         st.markdown('<h4>Correlation Matrix for bilioners in India</h4>', unsafe_allow_html=True)

    #         corr_india_df = df_india.copy()
    #         corr_india_df = corr_india_df.drop(columns = ['Name', 'Rank', 'Country / Region', 'Industry'])
    #         corr_india_df.corr()
    #         correlation_matrix_india = corr_india_df.corr()

    #         # Tworzenie wykresu macierzy korelacji
    #         plt.figure(figsize=(10, 8))
    #         sns.heatmap(correlation_matrix_india, annot=True, cmap='coolwarm', fmt='.2f')
    #         plt.title('Correlation Matrix')
    #         st.pyplot(plt)


    #         st.markdown('<h4>Interactive scaterplot for bilioners in India</h4>', unsafe_allow_html=True)

    #         df_filtered_india = df_india.copy()
    #         fig = px.scatter(
    #             df_filtered_india,
    #             x='Total net worth',
    #             y='$ YTD change',
    #             color='Industry',
    #             hover_name='Name',
    #             size='Total net worth',
    #             trendline='ols',
    #             labels={
    #                 'Total net worth': 'Net Worth (USD)',
    #                 '$ YTD change': 'Annual Change (USD)'
    #             },
    #             title='Growth in Income Relative to Assets for Various Industries',
    #             height=800,
    #             width=1100
    #         )
    #         for trace in fig.data:
    #             if trace.name != 'Technology':
    #                 trace.visible = 'legendonly'
    #         fig.update_layout(
    #             xaxis_title='Net Worth (USD)',
    #             yaxis_title='Annual Change (USD)',
    #             legend_title='Industry',
    #             template='plotly_white'
    #         )
    #         st.plotly_chart(fig, use_container_width=True)


    #         # # # # # # # #
    #         # STEP 4

    #         st.markdown('<h3 ># STEP 4: Outlier Analysis for India</h3>', unsafe_allow_html=True)

    #         st.markdown('<h4 >Boxplot of Total Net Worth of Billionaires in India</h4>', unsafe_allow_html=True)

    #         fig = px.box(
    #         df_india,
    #         x='Total net worth',
    #         title='Boxplot of Total Billionaire Net Worth of the estate',
    #         labels={'Total net worth': 'Total Net Worth of the estate (USD)'},
    #         height=800,
    #         width=1200
    #         )
    #         fig.update_layout(
    #             xaxis_title='Total Net Worth of the estate (USD)',
    #             template='plotly_white'
    #         )
    #         st.plotly_chart(fig, use_container_width=True)


    #         st.markdown('<h4 >Boxplot of Total Net Worth of Billionaires by Industry in India</h4>', unsafe_allow_html=True)

    #         fig = px.box(
    #             df_india,
    #             x='Total net worth',
    #             y='Industry',
    #             color='Industry',
    #             title='Boxplot of Total Net Worth of Billionaires by Industry in India',
    #             labels={
    #                 'Total net worth': 'Total Net Worth (USD)',
    #                 'Industry': 'Industry'
    #             },
    #             height=800,
    #             width=1200
    #         )
    #         for trace in fig.data:
    #             if trace.name != 'Technology':
    #                 trace.visible = 'legendonly'
    #         fig.update_layout(
    #             boxmode='group',
    #             xaxis_title='Total Net Worth (USD)',
    #             yaxis_title='Industry',
    #             template='plotly_white'
    #         )
    #         st.plotly_chart(fig, use_container_width=True)


    #         st.markdown('<h4 >Boxplot of last change net worth ($ Last change) for industries in India</h4>', unsafe_allow_html=True)

    #         fig = px.box(
    #             df_india,
    #             x='$ Last change',
    #             y='Industry',
    #             color='Industry',
    #             title='Boxplot of last change net worth ($ Last change) for industries in India',
    #             labels={
    #                 '$ Last change': 'Last Change (USD)',
    #                 'Industry': 'Industry'
    #             },
    #             height=800,
    #             width=1100
    #         )

    #         for trace in fig.data:
    #             if trace.name != 'Technology':
    #                 trace.visible = 'legendonly'

    #         fig.update_layout(
    #             boxmode='group',
    #             xaxis_title='Last Change (USD)',
    #             yaxis_title='Industry',
    #             template='plotly_white'
    #         )

    #         st.plotly_chart(fig, use_container_width=True)

    #         st.markdown('<h4 >Histogram of the number of bilioners of India</h4>', unsafe_allow_html=True)

    #         plt.figure(figsize=(14, 8))
    #         sns.histplot(df_india['Total net worth'], bins=80, kde=True)
    #         plt.title('Histogram of the number of bilioners of India')
    #         plt.xlabel('Total Net Worth')
    #         plt.ylabel('Number of occurrences')
    #         st.pyplot(plt)


    #     with tab3:
    #         st.markdown('<h3 ># STEP 1: General Overview of the Data for Rusia</h3>', unsafe_allow_html=True)
    #         # st.write(df_ready['Country / Region'].unique())
    #         df_russia = df_ready[df_ready['Country / Region'] == 'Russian Federation'].copy()
    #         df_russia

    #         # RESET INDEX

    #         buffer_russia = io.StringIO()
    #         df_russia.info(buf=buffer_russia)
    #         info_str_russia = buffer_russia.getvalue()

    #         ############
    #         # STEP 1
    #         # 

    #         # df_russia.info w Streamlit
    #         st.markdown('<h4>Basic information:</h4>', unsafe_allow_html=True)
    #         st.text(info_str_russia)

    #         st.markdown('<h4>Nunique values</h4>', unsafe_allow_html=True)
    #         st.write(df_russia.nunique())

    #         st.write(f'Unique values in total: {df_russia.nunique().sum()}')
    #         st.markdown('<h4>Descritive Statistics</h4>', unsafe_allow_html=True)
    #         st.write(df_russia.describe().T)

    #         st.markdown('<h3 ># STEP 2: Single Variable Analysis</h3>', unsafe_allow_html=True)
    #         st.markdown('<h4>Barplot for Bilioners in each industry in Rusia</h4>', unsafe_allow_html=True)


    #         industry_counts = df_russia['Industry'].value_counts()
    #         total_records = len(df_russia)
    #         percentage = (industry_counts / total_records) * 100

    #         plt.figure(figsize=(12, 6))
    #         bars = industry_counts.plot(kind='bar', color='skyblue', width=0.7)

    #         plt.ylim(0, industry_counts.max() + 20)
    #         plt.title('Number of Bilioners in each industry in Rusia', fontsize=16)
    #         plt.xlabel('Industry', fontsize=14)
    #         plt.ylabel('Number of Bilioners', fontsize=14)

    #         for bar, count, perc in zip(bars.patches, industry_counts, percentage):
    #             yval = bar.get_height()
    #             plt.text(bar.get_x() + bar.get_width()/2, yval + 5, f'{count}', ha='center', va='bottom', fontsize=12)
    #             plt.text(bar.get_x() + bar.get_width()/2, yval/2, f'{perc:.1f}%', ha='center', va='center', fontsize=12)

    #         plt.xticks(rotation=65, fontsize=12)
    #         plt.yticks(fontsize=12)
    #         plt.grid(axis='y', linestyle='--', alpha=0.7)
    #         plt.tight_layout()
    #         st.pyplot(plt)

    #         st.markdown('<h4>Barplot for Billionaires Total Net Worth by Industry in Rusia (USD Billion)</h4>', unsafe_allow_html=True)

    #         total_net_worth_ind_russia_df = df_russia.groupby('Industry', as_index=False)['Total net worth'].sum()
    #         total_net_worth_ind_russia_df = total_net_worth_ind_russia_df.sort_values(by='Total net worth', ascending=False).reset_index(drop=True)
    #         total_net_worth_ind_russia_df['Total net worth'] = (total_net_worth_ind_russia_df['Total net worth'] / 1e9).round(1)
    #         total_net_worth_ind_russia_df['Percentage'] = (total_net_worth_ind_russia_df['Total net worth'] / total_net_worth_ind_russia_df['Total net worth'].sum() * 100).round(1)
    #         plt.figure(figsize=(12, 8))
    #         bars = plt.bar(total_net_worth_ind_russia_df['Industry'], total_net_worth_ind_russia_df['Total net worth'], color='teal')
    #         for bar, value in zip(bars, total_net_worth_ind_russia_df['Total net worth']):
    #             plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f'{value}B', 
    #                     ha='center', va='bottom', fontsize=10)
    #         for bar, pct in zip(bars, total_net_worth_ind_russia_df['Percentage']):
    #             plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, f'{pct}%', 
    #                     ha='center', va='center', fontsize=10, color='white')
    #         plt.xticks(rotation=45, ha='right')
    #         plt.title('Billionaires Total Net Worth by Industry in Rusia (USD Billion)', fontsize=14)
    #         plt.xlabel('Industry')
    #         plt.ylabel('Net Worth (in USD billion)')
    #         y_max = total_net_worth_ind_russia_df['Total net worth'].max()
    #         plt.ylim(0, y_max * 1.15 if y_max > 0 else 1)
    #         plt.grid(axis='y', linestyle='--', alpha=0.7)
    #         plt.tight_layout()
    #         st.pyplot(plt)

    #         st.markdown('<h4>YTD net income of Millionaires in a given industry in Rusia</h4>', unsafe_allow_html=True)

    #         ytd_net_income_ind_russia_df = df_russia.groupby('Industry', as_index=False)['$ YTD change'].sum()
    #         ytd_net_income_ind_russia_df = ytd_net_income_ind_russia_df.sort_values(by='$ YTD change', ascending=False).reset_index(drop=True)
    #         ytd_net_income_ind_russia_df['$ YTD change'] = pd.to_numeric(ytd_net_income_ind_russia_df['$ YTD change'], errors='coerce').fillna(0)
    #         ytd_net_income_ind_russia_df['$ YTD change'] = (ytd_net_income_ind_russia_df['$ YTD change'] / 1e9).round(2)
    #         total_sum = ytd_net_income_ind_russia_df['$ YTD change'].sum()
    #         ytd_net_income_ind_russia_df['Percentage'] = (ytd_net_income_ind_russia_df['$ YTD change'] / total_sum * 100).round(1)
    #         plt.figure(figsize=(16, 8))
    #         bars = plt.bar(
    #             ytd_net_income_ind_russia_df['Industry'], 
    #             ytd_net_income_ind_russia_df['$ YTD change'], 
    #             color=['green' if val >= 0 else 'red' for val in ytd_net_income_ind_russia_df['$ YTD change']]
    #         )
    #         for bar, value, pct in zip(bars, ytd_net_income_ind_russia_df['$ YTD change'], ytd_net_income_ind_russia_df['Percentage']):
    #             height = bar.get_height()
    #             offset = 0.02 * plt.ylim()[1]
    #             plt.text(
    #                 bar.get_x() + bar.get_width() / 2, 
    #                 height + offset, 
    #                 f'{value}B', 
    #                 ha='center', va='bottom', fontsize=12
    #             )
    #             plt.text(
    #                 bar.get_x() + bar.get_width() / 2, 
    #                 height + 4 * offset, 
    #                 f'{pct}%', 
    #                 ha='center', va='bottom', fontsize=12
    #             )
    #         plt.xticks(rotation=45, ha='right')
    #         plt.title('Billionaires YTD Net Income by Industry (USD billion)', fontsize=14)
    #         plt.xlabel('Industry')
    #         plt.ylabel('Net revenue (in billion USD)')
    #         y_min = ytd_net_income_ind_russia_df['$ YTD change'].min()
    #         y_max = ytd_net_income_ind_russia_df['$ YTD change'].max()
    #         plt.ylim(
    #             y_min * 1.2 if y_min < 0 else -1,
    #             y_max * 1.35 if y_max > 0 else 1
    #         )
    #         plt.grid(axis='y', linestyle='--', alpha=0.7)
    #         plt.subplots_adjust(right=0.95, left=0.1, top=0.9, bottom=0.25)
    #         plt.tight_layout()
    #         st.pyplot(plt)

    #         st.markdown('<h3 ># STEP 3: Correlations</h3>', unsafe_allow_html=True)

    #         st.markdown('<h4>Correlation Matrix for bilioners in Rusia</h4>', unsafe_allow_html=True)

    #         corr_russia_df = df_russia.copy()
    #         corr_russia_df = corr_russia_df.drop(columns = ['Name', 'Rank', 'Country / Region', 'Industry'])
    #         corr_russia_df.corr()
    #         correlation_matrix_russia = corr_russia_df.corr()

    #         # Tworzenie wykresu macierzy korelacji
    #         plt.figure(figsize=(10, 8))
    #         sns.heatmap(correlation_matrix_russia, annot=True, cmap='coolwarm', fmt='.2f')
    #         plt.title('Correlation Matrix')
    #         st.pyplot(plt)


    #         st.markdown('<h4>Interactive scaterplot for bilioners in Rusia</h4>', unsafe_allow_html=True)

    #         df_filtered_russia = df_russia.copy()
    #         fig = px.scatter(
    #             df_filtered_russia,
    #             x='Total net worth',
    #             y='$ YTD change',
    #             color='Industry',
    #             hover_name='Name',
    #             size='Total net worth',
    #             trendline='ols',
    #             labels={
    #                 'Total net worth': 'Net Worth (USD)',
    #                 '$ YTD change': 'Annual Change (USD)'
    #             },
    #             title='Growth in Income Relative to Assets for Various Industries',
    #             height=800,
    #             width=1100
    #         )
    #         for trace in fig.data:
    #             if trace.name != 'Technology':
    #                 trace.visible = 'legendonly'
    #         fig.update_layout(
    #             xaxis_title='Net Worth (USD)',
    #             yaxis_title='Annual Change (USD)',
    #             legend_title='Industry',
    #             template='plotly_white'
    #         )
    #         st.plotly_chart(fig, use_container_width=True)


    #         # # # # # # # #
    #         # STEP 4

    #         st.markdown('<h3 ># STEP 4: Outlier Analysis for Rusia</h3>', unsafe_allow_html=True)

    #         st.markdown('<h4 >Boxplot of Total Net Worth of Billionaires in Rusia</h4>', unsafe_allow_html=True)

    #         fig = px.box(
    #         df_russia,
    #         x='Total net worth',
    #         title='Boxplot of Total Billionaire Net Worth of the estate',
    #         labels={'Total net worth': 'Total Net Worth of the estate (USD)'},
    #         height=800,
    #         width=1200
    #         )
    #         fig.update_layout(
    #             xaxis_title='Total Net Worth of the estate (USD)',
    #             template='plotly_white'
    #         )
    #         st.plotly_chart(fig, use_container_width=True)


    #         st.markdown('<h4 >Boxplot of Total Net Worth of Billionaires by Industry in Rusia</h4>', unsafe_allow_html=True)

    #         fig = px.box(
    #             df_russia,
    #             x='Total net worth',
    #             y='Industry',
    #             color='Industry',
    #             title='Boxplot of Total Net Worth of Billionaires by Industry in Rusia',
    #             labels={
    #                 'Total net worth': 'Total Net Worth (USD)',
    #                 'Industry': 'Industry'
    #             },
    #             height=800,
    #             width=1200
    #         )
    #         for trace in fig.data:
    #             if trace.name != 'Technology':
    #                 trace.visible = 'legendonly'
    #         fig.update_layout(
    #             boxmode='group',
    #             xaxis_title='Total Net Worth (USD)',
    #             yaxis_title='Industry',
    #             template='plotly_white'
    #         )
    #         st.plotly_chart(fig, use_container_width=True)


    #         st.markdown('<h4 >Boxplot of last change net worth ($ Last change) for industries in Rusia</h4>', unsafe_allow_html=True)

    #         fig = px.box(
    #             df_russia,
    #             x='$ Last change',
    #             y='Industry',
    #             color='Industry',
    #             title='Boxplot of last change net worth ($ Last change) for industries in Rusia',
    #             labels={
    #                 '$ Last change': 'Last Change (USD)',
    #                 'Industry': 'Industry'
    #             },
    #             height=800,
    #             width=1100
    #         )

    #         for trace in fig.data:
    #             if trace.name != 'Technology':
    #                 trace.visible = 'legendonly'

    #         fig.update_layout(
    #             boxmode='group',
    #             xaxis_title='Last Change (USD)',
    #             yaxis_title='Industry',
    #             template='plotly_white'
    #         )

    #         st.plotly_chart(fig, use_container_width=True)

    #         st.markdown('<h4 >Histogram of the number of bilioners of Rusia</h4>', unsafe_allow_html=True)

    #         plt.figure(figsize=(14, 8))
    #         sns.histplot(df_russia['Total net worth'], bins=80, kde=True)
    #         plt.title('Histogram of the number of bilioners of Rusia')
    #         plt.xlabel('Total Net Worth')
    #         plt.ylabel('Number of occurrences')
    #         st.pyplot(plt)


    #     with tab4:
    #         st.markdown('<h3 ># STEP 1: General Overview of the Data for Germany</h3>', unsafe_allow_html=True)
    #         # st.write(df_ready['Country / Region'].unique())
    #         df_germany = df_ready[df_ready['Country / Region'] == 'Germany'].copy()
    #         df_germany

    #         # RESET INDEX

    #         buffer_germany = io.StringIO()
    #         df_germany.info(buf=buffer_germany)
    #         info_str_germany = buffer_germany.getvalue()

    #         ############
    #         # STEP 1
    #         # 

    #         # df_germany.info w Streamlit
    #         st.markdown('<h4>Basic information:</h4>', unsafe_allow_html=True)
    #         st.text(info_str_germany)

    #         st.markdown('<h4>Nunique values</h4>', unsafe_allow_html=True)
    #         st.write(df_germany.nunique())

    #         st.write(f'Unique values in total: {df_germany.nunique().sum()}')
    #         st.markdown('<h4>Descritive Statistics</h4>', unsafe_allow_html=True)
    #         st.write(df_germany.describe().T)

    #         st.markdown('<h3 ># STEP 2: Single Variable Analysis</h3>', unsafe_allow_html=True)
    #         st.markdown('<h4>Barplot for Bilioners in each industry in Germany</h4>', unsafe_allow_html=True)


    #         industry_counts = df_germany['Industry'].value_counts()
    #         total_records = len(df_germany)
    #         percentage = (industry_counts / total_records) * 100

    #         plt.figure(figsize=(12, 6))
    #         bars = industry_counts.plot(kind='bar', color='skyblue', width=0.7)

    #         plt.ylim(0, industry_counts.max() + 20)
    #         plt.title('Number of Bilioners in each industry in Germany', fontsize=16)
    #         plt.xlabel('Industry', fontsize=14)
    #         plt.ylabel('Number of Bilioners', fontsize=14)

    #         for bar, count, perc in zip(bars.patches, industry_counts, percentage):
    #             yval = bar.get_height()
    #             plt.text(bar.get_x() + bar.get_width()/2, yval + 5, f'{count}', ha='center', va='bottom', fontsize=12)
    #             plt.text(bar.get_x() + bar.get_width()/2, yval/2, f'{perc:.1f}%', ha='center', va='center', fontsize=12)

    #         plt.xticks(rotation=65, fontsize=12)
    #         plt.yticks(fontsize=12)
    #         plt.grid(axis='y', linestyle='--', alpha=0.7)
    #         plt.tight_layout()
    #         st.pyplot(plt)

    #         st.markdown('<h4>Barplot for Billionaires Total Net Worth by Industry in Germany (USD Billion)</h4>', unsafe_allow_html=True)

    #         total_net_worth_ind_germany_df = df_germany.groupby('Industry', as_index=False)['Total net worth'].sum()
    #         total_net_worth_ind_germany_df = total_net_worth_ind_germany_df.sort_values(by='Total net worth', ascending=False).reset_index(drop=True)
    #         total_net_worth_ind_germany_df['Total net worth'] = (total_net_worth_ind_germany_df['Total net worth'] / 1e9).round(1)
    #         total_net_worth_ind_germany_df['Percentage'] = (total_net_worth_ind_germany_df['Total net worth'] / total_net_worth_ind_germany_df['Total net worth'].sum() * 100).round(1)
    #         plt.figure(figsize=(12, 8))
    #         bars = plt.bar(total_net_worth_ind_germany_df['Industry'], total_net_worth_ind_germany_df['Total net worth'], color='teal')
    #         for bar, value in zip(bars, total_net_worth_ind_germany_df['Total net worth']):
    #             plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f'{value}B', 
    #                     ha='center', va='bottom', fontsize=10)
    #         for bar, pct in zip(bars, total_net_worth_ind_germany_df['Percentage']):
    #             plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, f'{pct}%', 
    #                     ha='center', va='center', fontsize=10, color='white')
    #         plt.xticks(rotation=45, ha='right')
    #         plt.title('Billionaires Total Net Worth by Industry in Germany (USD Billion)', fontsize=14)
    #         plt.xlabel('Industry')
    #         plt.ylabel('Net Worth (in USD billion)')
    #         y_max = total_net_worth_ind_germany_df['Total net worth'].max()
    #         plt.ylim(0, y_max * 1.15 if y_max > 0 else 1)
    #         plt.grid(axis='y', linestyle='--', alpha=0.7)
    #         plt.tight_layout()
    #         st.pyplot(plt)

    #         st.markdown('<h4>YTD net income of Millionaires in a given industry in Germany</h4>', unsafe_allow_html=True)

    #         ytd_net_income_ind_germany_df = df_germany.groupby('Industry', as_index=False)['$ YTD change'].sum()
    #         ytd_net_income_ind_germany_df = ytd_net_income_ind_germany_df.sort_values(by='$ YTD change', ascending=False).reset_index(drop=True)
    #         ytd_net_income_ind_germany_df['$ YTD change'] = pd.to_numeric(ytd_net_income_ind_germany_df['$ YTD change'], errors='coerce').fillna(0)
    #         ytd_net_income_ind_germany_df['$ YTD change'] = (ytd_net_income_ind_germany_df['$ YTD change'] / 1e9).round(2)
    #         total_sum = ytd_net_income_ind_germany_df['$ YTD change'].sum()
    #         ytd_net_income_ind_germany_df['Percentage'] = (ytd_net_income_ind_germany_df['$ YTD change'] / total_sum * 100).round(1)
    #         plt.figure(figsize=(16, 8))
    #         bars = plt.bar(
    #             ytd_net_income_ind_germany_df['Industry'], 
    #             ytd_net_income_ind_germany_df['$ YTD change'], 
    #             color=['green' if val >= 0 else 'red' for val in ytd_net_income_ind_germany_df['$ YTD change']]
    #         )
    #         for bar, value, pct in zip(bars, ytd_net_income_ind_germany_df['$ YTD change'], ytd_net_income_ind_germany_df['Percentage']):
    #             height = bar.get_height()
    #             offset = 0.02 * plt.ylim()[1]
    #             plt.text(
    #                 bar.get_x() + bar.get_width() / 2, 
    #                 height + offset, 
    #                 f'{value}B', 
    #                 ha='center', va='bottom', fontsize=12
    #             )
    #             plt.text(
    #                 bar.get_x() + bar.get_width() / 2, 
    #                 height + 4 * offset, 
    #                 f'{pct}%', 
    #                 ha='center', va='bottom', fontsize=12
    #             )
    #         plt.xticks(rotation=45, ha='right')
    #         plt.title('Billionaires YTD Net Income by Industry (USD billion)', fontsize=14)
    #         plt.xlabel('Industry')
    #         plt.ylabel('Net revenue (in billion USD)')
    #         y_min = ytd_net_income_ind_germany_df['$ YTD change'].min()
    #         y_max = ytd_net_income_ind_germany_df['$ YTD change'].max()
    #         plt.ylim(
    #             y_min * 1.2 if y_min < 0 else -1,
    #             y_max * 1.35 if y_max > 0 else 1
    #         )
    #         plt.grid(axis='y', linestyle='--', alpha=0.7)
    #         plt.subplots_adjust(right=0.95, left=0.1, top=0.9, bottom=0.25)
    #         plt.tight_layout()
    #         st.pyplot(plt)

    #         st.markdown('<h3 ># STEP 3: Correlations</h3>', unsafe_allow_html=True)

    #         st.markdown('<h4>Correlation Matrix for bilioners in Germany</h4>', unsafe_allow_html=True)

    #         corr_germany_df = df_germany.copy()
    #         corr_germany_df = corr_germany_df.drop(columns = ['Name', 'Rank', 'Country / Region', 'Industry'])
    #         corr_germany_df.corr()
    #         correlation_matrix_germany = corr_germany_df.corr()

    #         # Tworzenie wykresu macierzy korelacji
    #         plt.figure(figsize=(10, 8))
    #         sns.heatmap(correlation_matrix_germany, annot=True, cmap='coolwarm', fmt='.2f')
    #         plt.title('Correlation Matrix')
    #         st.pyplot(plt)


    #         st.markdown('<h4>Interactive scaterplot for bilioners in Germany</h4>', unsafe_allow_html=True)

    #         df_filtered_germany = df_germany.copy()
    #         fig = px.scatter(
    #             df_filtered_germany,
    #             x='Total net worth',
    #             y='$ YTD change',
    #             color='Industry',
    #             hover_name='Name',
    #             size='Total net worth',
    #             trendline='ols',
    #             labels={
    #                 'Total net worth': 'Net Worth (USD)',
    #                 '$ YTD change': 'Annual Change (USD)'
    #             },
    #             title='Growth in Income Relative to Assets for Various Industries',
    #             height=800,
    #             width=1100
    #         )
    #         for trace in fig.data:
    #             if trace.name != 'Technology':
    #                 trace.visible = 'legendonly'
    #         fig.update_layout(
    #             xaxis_title='Net Worth (USD)',
    #             yaxis_title='Annual Change (USD)',
    #             legend_title='Industry',
    #             template='plotly_white'
    #         )
    #         st.plotly_chart(fig, use_container_width=True)


    #         # # # # # # # #
    #         # STEP 4

    #         st.markdown('<h3 ># STEP 4: Outlier Analysis for Germany</h3>', unsafe_allow_html=True)

    #         st.markdown('<h4 >Boxplot of Total Net Worth of Billionaires in Germany</h4>', unsafe_allow_html=True)

    #         fig = px.box(
    #         df_germany,
    #         x='Total net worth',
    #         title='Boxplot of Total Billionaire Net Worth of the estate',
    #         labels={'Total net worth': 'Total Net Worth of the estate (USD)'},
    #         height=800,
    #         width=1200
    #         )
    #         fig.update_layout(
    #             xaxis_title='Total Net Worth of the estate (USD)',
    #             template='plotly_white'
    #         )
    #         st.plotly_chart(fig, use_container_width=True)


    #         st.markdown('<h4 >Boxplot of Total Net Worth of Billionaires by Industry in Germany</h4>', unsafe_allow_html=True)

    #         fig = px.box(
    #             df_germany,
    #             x='Total net worth',
    #             y='Industry',
    #             color='Industry',
    #             title='Boxplot of Total Net Worth of Billionaires by Industry in Germany',
    #             labels={
    #                 'Total net worth': 'Total Net Worth (USD)',
    #                 'Industry': 'Industry'
    #             },
    #             height=800,
    #             width=1200
    #         )
    #         for trace in fig.data:
    #             if trace.name != 'Technology':
    #                 trace.visible = 'legendonly'
    #         fig.update_layout(
    #             boxmode='group',
    #             xaxis_title='Total Net Worth (USD)',
    #             yaxis_title='Industry',
    #             template='plotly_white'
    #         )
    #         st.plotly_chart(fig, use_container_width=True)


    #         st.markdown('<h4 >Boxplot of last change net worth ($ Last change) for industries in Germany</h4>', unsafe_allow_html=True)

    #         fig = px.box(
    #             df_germany,
    #             x='$ Last change',
    #             y='Industry',
    #             color='Industry',
    #             title='Boxplot of last change net worth ($ Last change) for industries in Germany',
    #             labels={
    #                 '$ Last change': 'Last Change (USD)',
    #                 'Industry': 'Industry'
    #             },
    #             height=800,
    #             width=1100
    #         )

    #         for trace in fig.data:
    #             if trace.name != 'Technology':
    #                 trace.visible = 'legendonly'

    #         fig.update_layout(
    #             boxmode='group',
    #             xaxis_title='Last Change (USD)',
    #             yaxis_title='Industry',
    #             template='plotly_white'
    #         )

    #         st.plotly_chart(fig, use_container_width=True)

    #         st.markdown('<h4 >Histogram of the number of bilioners of Germany</h4>', unsafe_allow_html=True)

    #         plt.figure(figsize=(14, 8))
    #         sns.histplot(df_germany['Total net worth'], bins=80, kde=True)
    #         plt.title('Histogram of the number of bilioners of Germany')
    #         plt.xlabel('Total Net Worth')
    #         plt.ylabel('Number of occurrences')
    #         st.pyplot(plt)