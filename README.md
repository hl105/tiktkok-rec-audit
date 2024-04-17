# tiktkok-rec-audit
Auditing TikTok's recommended videos section 
run code with: <br>

```
pytest -s explore_scroll.py  --html="report_test.html" --rs --uc --var1="Beauty"
```
--var1 options: Society, Sports, Food, Beauty <br>

### Troubleshooting
if you close your laptop / run into a failure / exit the terminal: close the terminal, open a new terminal, go to links.csv and delete the links that were already processed, and run the code again <br>
When the first round of opening a link -> explore page works, it should go smoothly from there <br>