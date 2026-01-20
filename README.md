# The 500 richest businessmen in the world
### About Dataset.

VBloomberg Billionaires Index.

View profiles for each of the world’s 500 richest people, see the biggest movers, and compare fortunes or track returns.As of December 12, 2024.

As of December 12, 2024.

The Bloomberg Billionaires Index is a daily ranking of the world’s richest people. Details about the calculations are provided in the net worth analysis on each billionaire’s profile page. The figures are updated at the close of every trading day in New York.

Columns: "Rank", "Name", "Total net worth", "Last change", "YTD change", "Country / Region", "Industry".

Sourse from Kaggle

Author of dataset

Licences CC
### From author of analize:

Columns: The analysis does not concern the economy, economic, political, geopolitycal, aspects, or sociological trends.The author`s objective was to find an interesting topic and conduct a simple Exploratory Data Analysis (EDA). In this case, the focus was on "The 500 richest businessmen in the world, aiming to identify an intriguing issue and present it in a straightforward manner. In addition to the overall analysis of billionaire assets, the work also includes tools for an analysis of countries such as the: USA, China, India, Russia, Germany

### Changes made:

## Analysis:
- All changes were implemented based on the original dataset without altering their values or substantive content.

The changes included:

- Converting numeric values written in shorthand (e.g., "447B") into readable numeric formats to facilitate calculations and readability.

- Removing unnecessary spaces from column names to simplify work.

### Refactor:
Przeprowadzić refaktoryzację kodu w sposób modularny. 

No DataFrame altered the original values.

Me

```
app/
│
├── app.py                  # entry point (Streamlit)
│
├── loader/
│   └── csv_loader.py           # load danych
|
├── data/
│   └──top_rich2024_ready.csv   # csv data
|
├── analysis/
│   ├── data_overwview.py       # universal compiuting for basic data overview
│   ├── statistics_for_countries.py # descriptive statistics for countrys analysis
│   └── statistics_for_global.py    # descriptive statistics for global analysis
│
│
├── visualization/
│   ├── plots.py            # plots for global analysis
│   └── plots_countrys.py   # plots for countrys analysis
│
├── ui/
│   ├── components          # sidebar global an countrys
|   |   └── data_overview.py  # render universal view for basic data overview
|   |
│   ├── sidebar.py          # sidebar uniwersal for all        
│   ├── components.py          # sidebar uniwersal for all        
|   |   |
|   |   └── data_overview.py   # basic overview for global and coutrys analysis
|   |
│   ├── pages.py/           # page/tab logic
│   |   |
│   |   ├── about.py        # Descryption of app
|   |   ├── global_analis.py    # global analysis
│   |   ├── about.py        # Descryption of app
|   |   └── countrys.py     # anasysis for countrys
|   |
|   └──styles.py            # Css style for all app
|
│
└── requirements.txt
```