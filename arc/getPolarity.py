from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

analyser = SentimentIntensityAnalyzer()

newsData = pd.read_csv("newsContent.txt",delimiter="|",header="infer") 
newsData['dateTime'] = pd.to_datetime(newsData['dateTime'])
numEvents = len(newsData.index) 

newsScore = [ analyser.polarity_scores(newsData.loc[i, "event"])["compound"] for i in range(numEvents) ]
newsScore = pd.Series(newsScore)
newsData["Score"] = newsScore

newsData.to_csv("eventsWithScores.txt")
