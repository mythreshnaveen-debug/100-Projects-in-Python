# Project 36 - Stock Trading App
# This time, I made a stock trading alert system.
# Use Case: Modify each one for every stock you are tracking, and make the script run when you boot up your system.
#  If there was a significant change in the stock, it gives some recent news headlines, and maybe some reasons why this big of a change occurred.

from math import floor

import requests
import datetime as time
from datetime import timedelta
from tkinter import messagebox

now = time.datetime.now()
yesterday = now - timedelta(days=1)
dby = now - timedelta(days=2)

def getNews():
    global yesterday
    newYesterday = f"{str(yesterday.year)}-{str(yesterday.month).zfill(2)}-{str(yesterday.day).zfill(2)}"
    response = requests.get(f"https://newsapi.org/v2/everything?q=Tesla%20Inc.&from={newYesterday}&sortBy=popularity&apiKey=d179a695b94545ee84dd476e5eb2777c")
    data = response.json()
    news = ""
    iteration = 0
    print(data['articles'])
    for article in data['articles']:
        iteration += 1
        if iteration == 4:
            break
        news += f"\"{article[("title")]}\" \n By:{article['author']}\n\n{article['content']}"
        if iteration != 3:
            news += "\n\n-----------\n"
    return news


response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&interval=5min&apikey=NUXR8H6BSNAD7F1L")
response.raise_for_status()
data = response.json()



timeY = f"{str(yesterday.year)}-{str(yesterday.month).zfill(2)}-{str(yesterday.day).zfill(2)}"
timeDBY = f"{str(dby.year)}-{str(dby.month).zfill(2)}-{str(dby.day).zfill(2)}"

priceY = data["Time Series (Daily)"][timeY]["4. close"]
priceDBY = data["Time Series (Daily)"][timeDBY]["4. close"]

print(timeY)

percent = ((float(priceY) - float(priceDBY))/float(priceDBY)) * 100

# print(timeY + ":\n" + priceY)
# print(timeDBY + ":\n" + priceDBY)
#
# print("\n" * 3)
#
# print(percent)
if percent > 5 or percent < -5:
    if percent > 5:
        message = f"""
TSLA: 🔺{floor(percent)}%
{getNews()}
"""
        messagebox.showinfo("STOCK CHANGE!", message)
    else:
        message = f"""
        TSLA: 🔻{abs(floor(percent))}%
        {getNews()}
        """
        messagebox.showinfo("STOCK CHANGE!", message)


#Optional: Format the SMS message like this:

