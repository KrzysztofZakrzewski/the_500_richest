import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# import statsmodels.api as sm
import io

from analysis.country_stats import country_counts_with_percentage
from visualization.plots import country_barplot

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

    # --- STEP 1 - General Overview 
     
    st.markdown('<h3 ># STEP 1: General Overview of the Data (Technical Aspects)</h3>', unsafe_allow_html=True)


    # df.info w Streamlit
    st.markdown('<h4>Basic information:</h4>', unsafe_allow_html=True)
    st.text(info_str)

    # cols and rows
    num_columns = df.shape[1]
    num_rows = df.shape[0]
    st.write(f"Columns: {num_columns}")
    st.write(f"Rows: {num_rows}")

    # nunique values
    st.markdown('<h4>Nunique values</h4>', unsafe_allow_html=True)
    st.write(df.nunique())

    st.markdown('<h4>Unique values in total:</h4>', unsafe_allow_html=True)
    unique_values_total = df.nunique().sum()
    st.write(f'{unique_values_total}')
    st.markdown('<p class="custom-text">No missing values</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">No duplicates</p>', unsafe_allow_html=True)

    # Descritive Statistics
    st.markdown('<h4>Descritive Statistics</h4>', unsafe_allow_html=True)
    st.write(df.describe().T)
    st.markdown('<p class="custom-text">STD is very hight in all columns about money</p>', unsafe_allow_html=True)

    # --- STEP 2 - STEP 2: Single Variable Analysis 

    st.markdown('<h3 ># STEP 2: Single Variable Analysis</h3>', unsafe_allow_html=True)

    # Barplot for Country / Region
    st.markdown('<h4>Barplot for Country / Region</h4>', unsafe_allow_html=True)
    

    counts, pct = country_counts_with_percentage(df)

    # --- Barplot of Numbers of Biloners for region
    fig = country_barplot(counts, pct)
    st.pyplot(fig)

    # 
    # Barplot for number of Bilioners in each industry
    # 

    st.markdown('<h4>Barplot for number of Bilioners in each industry</h4>', unsafe_allow_html=True)
    industry_counts = df['Industry'].value_counts()
    total_records = len(df)
    percentage = (industry_counts / total_records) * 100
    plt.figure(figsize=(12, 6))
    bars = industry_counts.plot(kind='bar', color='skyblue', width=0.7)
    plt.ylim(0, industry_counts.max() + 20)
    plt.title('Number of Bilioners in each industry', fontsize=16)
    plt.xlabel('Industry', fontsize=14)
    plt.ylabel('Number of Bilioners', fontsize=14)
    for bar, count, perc in zip(bars.patches, industry_counts, percentage):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 5, f'{count}', ha='center', va='bottom', fontsize=12)
        plt.text(bar.get_x() + bar.get_width()/2, yval/2, f'{perc:.1f}%', ha='center', va='center', fontsize=12)
    plt.xticks(rotation=65, fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(plt)

    #
    # Total Net Worth of Millionaires by Industry
    # 

    st.markdown('<h4>Total Net Worth of Millionaires by Industry</h4>', unsafe_allow_html=True)
    total_net_worth_ind_df = df.groupby('Industry', as_index=False)['Total net worth'].sum()
    total_net_worth_ind_df = total_net_worth_ind_df.sort_values(by='Total net worth', ascending=False).reset_index(drop=True)
    total_net_worth_ind_df

    # 
    # Barplot for Total Net Worth of Millionaires by Industry
    # 

    st.markdown('<h4>Barplot for Total Net Worth of Millionaires by Industry</h4>', unsafe_allow_html=True)

    total_net_worth_ind_df['Total net worth'] = (total_net_worth_ind_df['Total net worth'] / 1e9).round(1)
    total_net_worth_ind_df['Percentage'] = (total_net_worth_ind_df['Total net worth'] / total_net_worth_ind_df['Total net worth'].sum() * 100).round(1)
    plt.figure(figsize=(12, 8))
    bars = plt.bar(total_net_worth_ind_df['Industry'], total_net_worth_ind_df['Total net worth'], color='teal')
    for bar, value in zip(bars, total_net_worth_ind_df['Total net worth']):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f'{value}B', 
                ha='center', va='bottom', fontsize=10)
    for bar, pct in zip(bars, total_net_worth_ind_df['Percentage']):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, f'{pct}%', 
                ha='center', va='center', fontsize=10, color='white')
    plt.xticks(rotation=45, ha='right')
    plt.title('Billionaires Total Net Worth by Industry (USD Billion)', fontsize=14)
    plt.xlabel('Industry')
    plt.ylabel('Net Worth (in USD billion)')
    y_max = total_net_worth_ind_df['Total net worth'].max()
    plt.ylim(0, y_max * 1.15 if y_max > 0 else 1)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(plt)

    # 
    # YTD net income of Millionaires in a given industry
    #
    
    st.markdown('<h4>YTD net income of Millionaires in a given industry</h4>', unsafe_allow_html=True)
    ytd_net_income_ind_df = df.groupby('Industry', as_index=False)['$ YTD change'].sum()
    ytd_net_income_ind_df = ytd_net_income_ind_df.sort_values(by='$ YTD change', ascending=False).reset_index(drop=True)
    ytd_net_income_ind_df

    # Barplot for YTD net income of Millionaires in a given industry

    st.markdown('<h4>Barplot for YTD net income of Millionaires in a given industry</h4>', unsafe_allow_html=True)
    ytd_net_income_ind_df['$ YTD change'] = pd.to_numeric(ytd_net_income_ind_df['$ YTD change'], errors='coerce').fillna(0)
    ytd_net_income_ind_df['$ YTD change'] = (ytd_net_income_ind_df['$ YTD change'] / 1e9).round(2)
    total_sum = ytd_net_income_ind_df['$ YTD change'].sum()
    ytd_net_income_ind_df['Percentage'] = (ytd_net_income_ind_df['$ YTD change'] / total_sum * 100).round(1)
    plt.figure(figsize=(16, 8))
    bars = plt.bar(
        ytd_net_income_ind_df['Industry'], 
        ytd_net_income_ind_df['$ YTD change'], 
        color=['green' if val >= 0 else 'red' for val in ytd_net_income_ind_df['$ YTD change']]
    )
    for bar, value, pct in zip(bars, ytd_net_income_ind_df['$ YTD change'], ytd_net_income_ind_df['Percentage']):
        height = bar.get_height()
        offset = 0.02 * plt.ylim()[1]
        plt.text(
            bar.get_x() + bar.get_width() / 2, 
            height + offset,
            f'{value}B', 
            ha='center', va='bottom', fontsize=12
        )
        plt.text(
            bar.get_x() + bar.get_width() / 2, 
            height + 4 * offset,
            f'{pct}%', 
            ha='center', va='bottom', fontsize=12
        )
    plt.xticks(rotation=45, ha='right')
    plt.title('Billionaires YTD Net Income by Industry (USD billion)', fontsize=14)
    plt.xlabel('Industry')
    plt.ylabel('Net revenue (in billion USD)')
    y_min = ytd_net_income_ind_df['$ YTD change'].min()
    y_max = ytd_net_income_ind_df['$ YTD change'].max()
    plt.ylim(
        y_min * 1.2 if y_min < 0 else -1,
        y_max * 1.35 if y_max > 0 else 1
    )
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.subplots_adjust(right=0.95, left=0.1, top=0.9, bottom=0.25)
    plt.tight_layout()
    st.pyplot(plt)

    ############
    # STEP 3
    # 

    st.markdown('<h3 ># STEP 3: Correlations</h3>', unsafe_allow_html=True)
    st.markdown('<h4>Correlation Marix</h4>', unsafe_allow_html=True)

    corr_df = df.copy()
    corr_df = corr_df.drop(columns = ['Name', 'Rank', 'Country / Region', 'Industry'])
    corr_df.corr()
    st.write(corr_df.corr())

    correlation_matrix = corr_df.corr()

    # Tworzenie wykresu macierzy korelacji
    plt.figure(figsize=(6, 4))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
            
    st.pyplot(plt)

    st.markdown('<p class="custom-text">Very strong correlation between: "YTD change" and "Total net worth" at 0.82. Strong correlation between:YTD change and Last change at 0.79Moderately strong correlation between:Last change and Total net worth at 0.65. </p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Strong correlation between: "YTD change" and "Last change" at 0.79.</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Moderately strong correlation between: "Last change" and "Total net worth" at 0.65.</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Moderately strong correlation between: "Last change" and "Total net worth" at 0.65.</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">💲We can jokingly risk saying that money attracts money💰.</p>', unsafe_allow_html=True)

    # 
    ## Interactive scaterplot
    # 
    st.markdown('<h4>Interactive scaterplot</h4>', unsafe_allow_html=True)

    df_filtered = df.copy()
    fig = px.scatter(
        df_filtered,
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
    for trace in fig.data:
        if trace.name != 'Technology':
            trace.visible = 'legendonly'
    fig.update_layout(
        xaxis_title='Net worth (USD)',
        yaxis_title='Annual change (USD)',
        legend_title='Industry',
        template='plotly_white'
    )
    st.plotly_chart(fig)

    # 
    # STEP 4: Outlier Analysis
    #
    
    st.markdown('<h3 ># STEP 4: Outlier Analysis</h3>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">Boxplot of Total Billionaire Net Worth of the estate</p>', unsafe_allow_html=True)
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
    st.plotly_chart(fig)


    # Boxplot Billionaires by Industry

    st.markdown('<h4>Boxplot of Billionaires by Industry</h4>', unsafe_allow_html=True)

    fig = px.box(
        df,
        x='Total net worth',
        y='Industry',
        color='Industry',
        title='Boxplot of Total Net Worth of Billionaires by Industry',
        labels={
            'Total net worth': 'Total net worth (USD)',
            'Industry': 'Industry'
        },
        height=800,
        width=1200
    )
    for trace in fig.data:
        if trace.name != 'Technology':
            trace.visible = 'legendonly'
    fig.update_layout(
        boxmode='group',
        xaxis_title='Total net worth',
        yaxis_title='Industry',
        template='plotly_white'
    )
    st.plotly_chart(fig)

    # Boxplot Billionaires by Industry
    st.markdown('<h4>Boxplot of YDT Billionaires by Industry</h4>', unsafe_allow_html=True)

    fig = px.box(
        df,
        x='$ YTD change',
        y='Industry',
        color='Industry',
        title='Boxplot of annual net worth income of billionaires ($ YTD change) by industry',
        labels={
            '$ YTD change': 'YTD change (USD)',
            'Industry': 'Industry'
        },
        height=800,
        width=1200 
    )
    for trace in fig.data:
        if trace.name != 'Technology':
            trace.visible = 'legendonly'
    fig.update_layout(
        boxmode='group',
        xaxis_title='YTD change (USD)',
        yaxis_title='Industry',
        template='plotly_white'
    )
    st.plotly_chart(fig)

    st.markdown('<h4>Boxplot of last change net worth ($ Last change) for industries</h4>', unsafe_allow_html=True)

    fig = px.box(
        df,
        x='$ Last change',
        y='Industry',
        color='Industry',
        title='Boxplot of last change net worth ($ Last change) for industries',
        labels={
            '$ Last change': 'Last change (USD)',
            'Industry': 'Industry'
        },
        height=800,
        width=1100
    )
    for trace in fig.data:
        if trace.name != 'Technology':
            trace.visible = 'legendonly'
    fig.update_layout(
        boxmode='group',
        xaxis_title='Last change (USD)',
        yaxis_title='Industry',
        template='plotly_white'
    )
    st.plotly_chart(fig)

    # Outliners calculations

    st.markdown('<h4>Outliner calculations</h4>', unsafe_allow_html=True)
    df_outliners = df.drop(columns = ['Name', 'Rank', 'Country / Region', 'Industry'])
    
    def detect_outliers_iqr(df_outliners):
        outliers = {}
        for column in df_outliners.select_dtypes(include=[float, int]).columns:
            Q1 = df_outliners[column].quantile(0.25)
            Q3 = df_outliners[column].quantile(0.75)
            IQR = Q3 - Q1
            
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers[column] = df_outliners[(df_outliners[column] < lower_bound) | (df_outliners[column] > upper_bound)]
        return outliers
    
    outliers = detect_outliers_iqr(df_outliners)

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
