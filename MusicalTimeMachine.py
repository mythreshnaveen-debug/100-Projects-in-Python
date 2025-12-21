#Project 46 - Musical Time Machine
# This again uses the Beautiful Soup API to Scrape the music that was most popular at a specific time period, and return them back
# to you.

from bs4 import BeautifulSoup
import requests

year = input("Year: ")
month = input("Month: ")
day = input("Day: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

for t in soup.find_all('div'):
    if t.get('class') and t.get('class')[0] == "o-chart-results-list-row-container":
        soup = BeautifulSoup(str(t), "html.parser")
        for t2 in soup.find_all('h3'):
            if t2.get('id') == "title-of-a-story":
                print(t2.contents[0][14:][:-5])
                break
