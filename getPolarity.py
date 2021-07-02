from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

analyser = SentimentIntensityAnalyzer()

newsData = pd.read_csv("eventsData.txt",delimiter=",",header="infer") 
newsData['datetime'] = pd.to_datetime(newsData['datetime'])
numEvents = len(newsData.index) 

newsScore = [ analyser.polarity_scores(newsData.loc[i, "news"])["compound"] for i in range(numEvents) ]
newsScore = pd.Series(newsScore)
newsData["Score"] = newsScore

newsData.to_csv("eventsWithScores.txt")
