import streamlit as st

#==============
# RENDER ABOUT
#==============

def render_about() -> None:
    # st.header("About")
    st.markdown('<h1 class="custom-title">The 500 richest businessmen in the world</h1>', unsafe_allow_html=True)

    st.markdown('<h3 >About Dataset.</h3>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">VBloomberg Billionaires Index.</p>', unsafe_allow_html=True)


    st.markdown('<p class="custom-text">View profiles for each of the world’s 500 richest people, see the biggest movers, and compare fortunes or track returns.As of December 12, 2024.</p>', unsafe_allow_html=True)


    st.markdown('<p class="custom-text">As of December 12, 2024.</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">The Bloomberg Billionaires Index is a daily ranking of the world’s richest people. Details about the calculations are provided in the net worth analysis on each billionaire’s profile page. The figures are updated at the close of every trading day in New York.</p>', unsafe_allow_html=True)

    st.markdown('<p class="custom-text">Columns: "Rank", "Name", "Total net worth", "Last change", "YTD change", "Country / Region", "Industry".</p>', unsafe_allow_html=True)
    st.markdown("[Sourse from Kaggle](https://www.kaggle.com/datasets/mahmoudredagamail/the-worlds-500-most-powerful-businessmen)")
    st.markdown("[Author of dataset](https://www.kaggle.com/mahmoudredagamail/datasets)")
    st.markdown("[Licences CC](https://creativecommons.org/licenses/by/4.0/)")

    st.markdown('<h3 >From author of analize:</h3>', unsafe_allow_html=True)

    st.markdown('<p class="custom-text">Columns: The analysis does not concern the economy, economic, political, geopolitycal, aspects, or sociological trends.The author`s objective was to find an interesting topic and conduct a simple Exploratory Data Analysis (EDA). In this case, the focus was on "The 500 richest businessmen in the world, aiming to identify an intriguing issue and present it in a straightforward manner. In addition to the overall analysis of billionaire assets, the work also includes tools for an analysis of countries such as the: USA, China, India, Russia, Germany</p>', unsafe_allow_html=True)

    st.markdown('<h3 >Changes made:</h3>', unsafe_allow_html=True)

    st.markdown('<p class="custom-text">- All changes were implemented based on the original dataset without altering their values or substantive content.</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">The changes included:</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">- Converting numeric values written in shorthand (e.g., "447B") into readable numeric formats to facilitate calculations and readability.</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">- Removing unnecessary spaces from column names to simplify work.</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-text">No DataFrame altered the original values.</p>', unsafe_allow_html=True)

    st.markdown("[Me](https://github.com/KrzysztofZakrzewski)")