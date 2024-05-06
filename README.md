# tiktkok-rec-audit

## Data Collection
Data Scraping code is in the `scraper` folder. <br>
Auditing TikTok's recommended videos section 
run code with: <br>

```
pytest -s scraper/explore_scroll.py  --html="report_test.html" --rs --uc --var1="Beauty"
```
--var1 options: Society, Sports, Beauty <br>

The Pyktok module was modified to add `suggested words` and `diversification labels`. The source code is in the folder `Pyktok`. The module can be run with the file `pyktok-collect.py`
## Data Cleaning and Analysis
All files related to data cleaning are in the `data` folder. <br>
Notebooks related to data anlaysis methods that were selected are in the main path. <br>
e.g. `jaccard_analysis.ipynb` <br>
Data analysis methods that were attempted but not selected are in the `attempted_methods` folder.
