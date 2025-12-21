#Day 45 - Daily News
# This uses the BeautifulSoup API to get all of the top headlines on hacker news for today, and say which one
# has been upvoted the most.

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

names = []
hrefs = []
points = []

for t in soup.find_all('span'):
    if t.attrs.get('class') and t.attrs.get('class')[0] == "titleline":
        aTag = t.contents[0]
        names.append(aTag.text)
        hrefs.append(aTag.attrs.get('href'))
    elif t.attrs.get('class') and t.attrs.get('class')[0] == "score":
        points.append(int(t.text.split(" ")[0]))
for i in range(len(points)):
    if points[i]:
        print(names[i] + ": " + hrefs[i] + " (" + str(points[i]) + " upvotes)")

print("MOST UPVOTED:")

# Finding most upvoted list
largestIndex = 0
currentIndex = 0
lUV = -100
for num in points:
    if lUV < num:
        largestIndex = currentIndex
        lUV = num
    currentIndex += 1
print(names[largestIndex] + ": " + hrefs[largestIndex] + " (" + str(lUV) + " upvotes)")
