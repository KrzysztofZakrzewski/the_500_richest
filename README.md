# the_500_richest

```
app/
│
├── app.py                  # entry point (Streamlit)
│
├── loader/
│   ├── loader.py           # ładowanie danych
|
├── data/
│   └──top_rich2024_ready.csv
|
├── analysis/
│   ├── stats.py            # statystyki opisowe
│   ├── models.py           # modele ML
│
├── visualization/
│   ├── charts.py           # wykresy
│   ├── tables.py
│
├── ui/
│   ├── sidebar.py          # sidebar
│   ├── pages.py/           # logika stron / zakładek
│   |   ├── about.py
|   |   ├── global_analis.py
|   |   └── countrys.py
|   |
|   └──styles.py   
|
├── utils/
│   ├── config.py
│   ├── helpers.py
│
└── requirements.txt
```