import streamlit as st
import pandas as pd
import io

#==============
# --- Inner Imports
#==============
from analysis.statistics_for_global import (country_counts_with_percentage,
                                    compute_industry_counts,
                                    compute_total_net_worth_by_industry,
                                    aggregate_net_worth_by_industry,
                                    compute_ytd_net_income,
                                    aggregate_ytd_net_income,
                                    compute_correlation,
                                    detect_outliers_iqr)

from visualization.plots import (country_barplot,
                                 industry_barplot,
                                 industry_net_worth_barplot,
                                 ytd_net_income_barplot,
                                 coutry_plot_correlation_matrix,
                                 plot_growth_vs_assets,
                                 plot_total_net_worth_box,
                                 universal_plot_box_by_industry)

from analysis.data_overview import compute_basic_overview
from ui.components.data_overview import render_basic_overview

#==============
# RENDER GLOBAL ANALIS
#==============

def render_global_analysis(df: pd.DataFrame) -> None:
    st.header("Global analysis")
    st.markdown('<h1 class="custom-title">The 500 richest businessmen in the world</h1>', unsafe_allow_html=True)
    st.markdown('<h2 >Global analysis</h2>', unsafe_allow_html=True)


    buffer = io.StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()

    #==============
    # EDA
    #==============
    
    #==============
    # --- STEP 1 - General Overview 
     
    st.markdown('<h3> STEP 1: General Overview of the Data (Technical Aspects)</h3>', unsafe_allow_html=True)

    # --- Compiuting and rendering basic overview
    overview = compute_basic_overview(df)
    render_basic_overview(df, overview, info_str)

    #==============
    # --- STEP 2 - STEP 2: Single Variable Analysis 

    st.markdown('<h3 ># STEP 2: Single Variable Analysis</h3>', unsafe_allow_html=True)

    # Barplot for Country / Region
    st.markdown('<h4>Barplot for Country / Region</h4>', unsafe_allow_html=True)
    
    # Compiuting stats for plot of number of Biloners
    country_counts, country_pct = country_counts_with_percentage(df)

    # --- Barplot of Numbers of Biloners for region
    fig = country_barplot(country_counts, country_pct)
    st.pyplot(fig)

    # --- Barplot for number of Bilioners in each industry
    st.markdown('<h4>Barplot for number of Bilioners in each industry</h4>', unsafe_allow_html=True)
    industry_counts, industry_percentage = compute_industry_counts(df)
    fig = industry_barplot(industry_counts, industry_percentage)
    st.pyplot(fig)

    # --- Total Net Worth of Millionaires by Industry
    st.markdown('<h4>Total Net Worth of Millionaires by Industry</h4>', unsafe_allow_html=True)
    total_net_worth_ind_df = aggregate_net_worth_by_industry(df)
    # st.dataframe(total_net_worth_ind_df) 
    
    # --- Barplot for Total Net Worth of Millionaires by Industry
    st.markdown('<h4>Barplot for Total Net Worth of Millionaires by Industry</h4>', unsafe_allow_html=True)
    net_worth_df = compute_total_net_worth_by_industry(total_net_worth_ind_df)
    fig = industry_net_worth_barplot(net_worth_df)
    st.pyplot(fig)
 
    # --- YTD net income of Millionaires in a given industry
    st.markdown('<h4>YTD net income of Millionaires in a given industry</h4>', unsafe_allow_html=True)
    ytd_net_income_ind_df = aggregate_ytd_net_income(df)

    # --- Barplot for YTD net income of Millionaires in a given industry
    st.markdown('<h4>Barplot for YTD net income of Millionaires in a given industry</h4>', unsafe_allow_html=True)
    ytd_df = compute_ytd_net_income(ytd_net_income_ind_df)
    fig = ytd_net_income_barplot(ytd_df)
    st.pyplot(fig)

    #===========
    # --- STEP 3 - Correlations

    st.markdown('<h3>STEP 3: Correlations</h3>', unsafe_allow_html=True)
    st.markdown('<h4>Correlation Marix</h4>', unsafe_allow_html=True)
    # --- Compiuting Matrix
    corr_matrix = compute_correlation(df)
    st.dataframe(corr_matrix)

    # --- Matrix Plot
    fig = coutry_plot_correlation_matrix(corr_matrix)
    st.pyplot(fig)

    st.markdown('<p class="custom-text">Very strong correlation between: "YTD change" and "Total net worth" at 0.82. Strong correlation between:YTD change and Last change at 0.79Moderately strong correlation between:Last change and Total net worth at 0.65. </p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Strong correlation between: "YTD change" and "Last change" at 0.79.</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Moderately strong correlation between: "Last change" and "Total net worth" at 0.65.</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Moderately strong correlation between: "Last change" and "Total net worth" at 0.65.</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">💲We can jokingly risk saying that money attracts money💰.</p>', unsafe_allow_html=True)

    #==============
    # INTERACITVE SCATERPLOTS
    #==============
    st.markdown('<h4>Interactive scaterplot</h4>', unsafe_allow_html=True)

    fig = plot_growth_vs_assets(df)
    st.plotly_chart(fig)

    #==============
    # STEP 4: Outlier Analysis
    st.markdown('<h3>STEP 4: Outlier Analysis</h3>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Boxplot of Total Billionaire Net Worth of the estate</p>', unsafe_allow_html=True)

    #--- Create a boxplot of total net worth for all billionaires.
    fig = plot_total_net_worth_box(df)
    st.plotly_chart(fig)

    # --- Boxplot Billionaires by Industry
    st.markdown('<h4 >Boxplot of Billionaires by Industry</h4>', unsafe_allow_html=True)


    fig = universal_plot_box_by_industry(
        df,
        x_col='Total net worth',
        title='Total Net Worth of Billionaires by Industry',
        x_label='Total net worth (USD)',
        highlight_industry='Technology'
    )
    st.plotly_chart(fig)



    # --- Boxplot Billionaires by Industry
    st.markdown('<h4>Boxplot of YDT Billionaires by Industry</h4>', unsafe_allow_html=True)

    fig = universal_plot_box_by_industry(
        df,
        x_col='$ YTD change',
        title='Annual Net Worth Change ($ YTD) by Industry',
        x_label='YTD change (USD)',
        highlight_industry='Technology'
    )
    st.plotly_chart(fig)

    st.markdown('<h4>Boxplot of last change net worth ($ Last change) for industries</h4>', unsafe_allow_html=True)

    # --- Boxplot of last change net worth ($ Last change)
    fig = universal_plot_box_by_industry(
        df,
        x_col='$ Last change',
        title='Annual Net Worth Change ($ YTD) by Industry',
        x_label='$ Last change',
        highlight_industry='Technology'
    )
    st.plotly_chart(fig)

    # --- Outliners calculations
    st.markdown('<h4>Outliner calculations</h4>', unsafe_allow_html=True)
    outliers = detect_outliers_iqr(df)

    for column, outlier_data in outliers.items():
        st.write(f'Column: {column} have {len(outlier_data)} outliers.')


    st.markdown('<h2 ># Summary of the overall analysiss</h2>', unsafe_allow_html=True)
    st.markdown('<h4>Conclusions:</h4>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">First Glance</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Regarding industries:</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">The largest number of billionaires operates in the technology industry. Specifically, 83 individuals, representing 16.6% of the dataset population.  Interestingly, they collectively hold 31.3% of the wealth, amounting to 3,142.1 billion USD out of the total 500 billionaires.</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Their annual income in 2024 was 962.94 billion USD, constituting an impressive 54.2% of the total income of all 500 billionaires. Regarding total wealth across industries: We can distinguish four groups based on their total wealth, categorized as follows:</p>', unsafe_allow_html=True)

    st.markdown('<p class="custom-text">A. From 9.7% to 8.1%:<br>- Industrial<br>- Financial<br>- Retail<br>- Diversified</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">B. 4.9%:<br>- Energy</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">C. From 3.8% to 2.9%:<br>- Food & Beverages<br>- Healthcare<br>- Real Estate<br>- Commodities</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">D. From 2.1% to 1.5%:<br>- Media & Telecommunications<br>- Services<br>- Entertainment</p>', unsafe_allow_html=True)
    
    st.markdown('<h4>Regarding billionares net income:</h4>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">In addition to the technology sector, two other industries stand out:<br>- Retail: 219.94 billion USD, 12%<br>- Financial: 213.05 billion USD, 12%</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Following them:<br>- Industrial: 104.39 billion USD, 5.9%</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Other industries:<br>- Diversified<br>- Energy<br>- Healthcare<br>- Services<br>- Real Estate<br>- Media & Telecommunications<br>- Entertainment range from 3.7% to 1.2%.</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">The last industry that generated a profit:<br>- Food & Beverages: $5.65 billion USD, 0.3%</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Industries with negative income:<br>- Consumer: -3.24 billion USD, -0.2%<br>- Commodities: -3.41 billion USD, -0.2%</p>', unsafe_allow_html=True)

    st.markdown('<h4>Correlations:</h4>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Very strong correlation between:<br>- "YTD change" and "Total net worth" at 0.82.</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Strong correlation between:<br>- "YTD change" and "Last change" at 0.79.</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Moderately strong correlation between:<br>- "Last change" and "Total net worth" at 0.65.</p>', unsafe_allow_html=True)
    
    st.markdown('<h4>Trends:</h4>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Based on the charts, the following trends can be observed:</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">There is a noticeable negative correlation between "Total net worth" and "$ YTD change" in the "Consumer" industry, as well as a less pronounced negative correlation in "Food & Beverages".</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Positive but weak correlation exists in industries:<br>- Diversified<br>- Energy<br>- Industrial<br>- Real Estate<br>- Commodities<br>- Entertainment</p>', unsafe_allow_html=True)
    
    st.markdown('<h4>Outliers:</h4>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">- "Total net worth" has 55 outliers.<br>- "Last change" has 83 outliers.<br>- "YTD change" has 63 outliers.</p>', unsafe_allow_html=True)
    st.markdown('<h3>No outliers were observed in the following cases:</h3>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Total net worth for billionaires in two industries:<br>- Commodities<br>- Real Estate</p>', unsafe_allow_html=True)

    st.markdown('<p class="custom-text">Annual net income of billionaires in four industries:<br>- Food & Beverages<br>- Entertainment<br>- Real Estate<br>- Services</p>', unsafe_allow_html=True)

    st.markdown('<p class="custom-text">Changes in last change:</p>', unsafe_allow_html=True)

    st.markdown('<p class="custom-text">No outliers were detected for two industries:<br>- Commodities<br>- Real Estate</p>', unsafe_allow_html=True)
