import streamlit as st
import pandas as pd


stockName = st.text_input("Give me a stock name: ")

df = pd.read_csv("eventsWithScores.txt") 

myReturns = df[df['event'].str.contains(stockName)]

if not myReturns.empty:
    st.write("Score for your stock is " + str(myReturns["Score"].mean() ) )
else: 
    st.write("Stock not found")
