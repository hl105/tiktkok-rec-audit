# tiktkok-rec-audit


## Data Collection
Data Scraping code is in the `scraper` folder. <br>
Auditing TikTok's recommended videos section 
run code with: <br>

```
pytest -s scraper/explore_scroll.py  --html="report_test.html" --rs --uc --var1="Beauty"
```
--var1 options: Society, Sports, Beauty <br>

## Data Analysis
All files related to data cleaning, data analysis are in the `Data` folder.
