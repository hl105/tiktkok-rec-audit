# tiktkok-rec-audit

## Data Collection
Data Scraping code is in the `scraper` folder. <br>
Auditing TikTok's recommended videos section 
run code with: <br>

```
pytest -s scraper/explore_scroll.py  --html="report_test.html" --rs --uc --var1="Beauty"
```
--var1 options: Society, Sports, Beauty <br>

## Data Cleaning and Analysis
All files related to data cleaning are in the `Data` folder. <br>
Notebooks related to data anlaysis methods that were selected are in the main path. <br>
e.g. `jaccard_analysis.ipynb` <br>
Data analysis methods that were attempted but not selected are in the `attempted_methds` folder.

