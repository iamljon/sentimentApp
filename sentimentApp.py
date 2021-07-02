from numpy.lib.arraysetops import unique
import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

st.title("Sentiment Detection")

df = pd.read_csv("eventsWithScores.txt") 
uniqueTickers = df.ticker.unique() 
uniqueTickers.sort()

option = st.selectbox('Choose your ticker', uniqueTickers )

idx = df['ticker'].str.contains(option)
myReturns = df.loc[ idx, ["datetime", "news","score"] ]

st.write( myReturns )
