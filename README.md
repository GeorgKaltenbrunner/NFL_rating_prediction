# NFL_rating_prediction
Scraping data from the web and predicting the players ratings using Machine Learning models

## Information
- First from https://www.nfl.com/stats/player-stats/category/passing/1970/reg/all/passingyards/desc data was scraped.
- Secondly the data was analyzed.
- Thirdly the data was used to predict the players rating with LineaRegression, RandomForest, HuberRegression. To validate the predictions r2, mse and mae were applied.

#### CollectData.py
Here the data is collected. This is done by using beautifulsoup and then scraping the information needed per page. Pagination is also done. The collected data is stored in a pandas DataFrame that is at the end exportet as csv file.

#### EPA.py
Here functions to analyse the data are written.

#### MLmodels.py
Here LinearRegression, RandomForest and HuberRegression can be found.