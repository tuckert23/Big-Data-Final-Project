# Computational Analysis of Big Data
## Final Project  
Computational Analysis of Big Data  
DIS Copenhagen  
December 6, 2021  
Lucian Leahu and Daniel Svendsen  

## Contributors:
Chichi Wu, Mariana Zamorano, Nate Harris, and Taylor Tucker

## Research Question:
Is it possible to predict the winner of The Bachelorette using public opinion data from Twitter. 

## Link to Medium Blog Post


## Description of Notebooks
- __Wikipedia Master Code.ipynb__
This notebook scrapes, processes, combines, and saves data from tables across various Wikipedia sites, primarily through the Wikipedia API, which we accessed using Beautiful Soup. 

- __tweet_scraper.py__
This Python script scrapes tweets from Twitter using a cross-referenced list of dates from the Wikipedia Master Code notebook. Unfortunately, due to security concerns, this script is not functional. However, the results of the scrapping are saved in the .zip file.

- __Sentiment Analysis.ipynb__
This notebook takes the results of tweet_scraper.py, along with the Wikipedia code, and performs sentiment analysis throught the NLTK package. This data is stored in the file twitter_data_not_manually_cleaned.csv. We had to manually go through a fix a few artifacts, and the full clean twitter data can be found in the tweets_clean.csv file. Said artifacts are that some of the seasons were not copied over, which takes only 45 seconds to fix manually. 

- __Model.ipynb__
This notebook is where we pull together everything from both the Twitter and Wikipedia .csv files. The code should work as-is with the provided datasets (i.e. there is no need to run any of the previous three files in order to perform some of the analysis). The model first takes the data and encodes it so that a simple neural network can make use of it. Then, the notebook builds and executes the simple neural network on the data, season-by-season, and its results can be seen in the last code cell.

## Package requirements
- numpy
- pandas
- matplotlib.pyplot
- nltk.sentiment.vader.SentimentIntensityAnalyzer
- datetime.datetime
- datetime.timedelta
- re
- tweepy
- requests
- bs4.BeautifulSoup
- collections.defaultdict
- os
- tensorflow
- keras
- keras
- time
