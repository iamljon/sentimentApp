import requests
from bs4 import BeautifulSoup
import time
import random



def getMyData(count, f):

    url = "https://seekingalpha.com/market-news/" + str(count) 
    print(url)

    response = requests.get(url).content
    soup = BeautifulSoup(response, features="html.parser")
    soupH4 = soup.find_all("li",  {"class":"item"} )

    numEvents = len(soupH4)
    print(numEvents)

    for j in range(numEvents) :

        data = str(soupH4[j]).split(" ")
        try:        
            eventDate = data[2][16:]
            eventTime = data[3]
            eventDetails = data[7][20:].replace("-", " ").replace('"','')
            
            f.write(eventDate +" "+ eventTime + "|" + eventDetails + "\n")

            # print(eventDate +" "+ eventTime + "|" + eventDetails )

        except:
            print("skip this one")



f = open("newsContent.txt", "a")


for count in range(1,2001):
    getMyData(count, f)
    time.sleep(random.randint(0,7))

f.close()
