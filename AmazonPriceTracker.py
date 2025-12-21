#Project 47 - Amazon Price Tracker
# This alerts the user if an item they like is below a certain price.

# To use: edit the variables: webpage, targetPrice, and nameOfItem.
# Save this script, and put it in shell.startup (or whatever place your OS runs code from when your system is booted up.)
# It's also recommended to make this script run twice, as sometimes Amazon gives you a captcha.
import re

from bs4 import BeautifulSoup
import requests
from tkinter import messagebox

webpage = "https://www.amazon.com/Apple-2025-MacBook-15-inch-Laptop/dp/B0DZD8BT7N?ref_=ast_sto_dp&th=1" #Amazon Link
targetPrice = 5000#Price that (if the item's price is below) it will alert you.
nameOfItem = "MacBook"#Nickname, just in case you have multiple of these.


header = { #Not actually my real system specs, borrowed it online; this is used for authentication im guessing, as
    # Amazon never showed the price of an item unless I added these.
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(webpage, headers=header)
tWP = response.text

soup = BeautifulSoup(tWP, 'html.parser')

#with open("webpage.html", "w", encoding="utf-8") as file:
#    file.truncate(0)
#    file.write(response.text) #(When i was testing, I kept on using the webpage as a reference, as Amazon tends to add extra stuff.

price = 0

index = 1

# This thing exists, since amazon has some *hidden* prices which mess up finding the actual price.
foundPrice1 = False
foundPrice2 = False

for t in soup.find_all('span'):
    table = list(soup.find_all('span'))
    percent = (index / len(table)) * 100
    print("Sorting through code: [" + "#" * int(percent / 10) + "] (" + str(round(percent, 3)) + "%)")
    index += 1

    if t.attrs.get('class') and t.attrs.get('class')[0] == "a-price-whole" and not foundPrice1:
        text = re.sub(r'[^a-zA-Z0-9]', '', t.text) #W3 schools is a lifesaver for stuff like this
        price = float(text)
        foundPrice1 = True
    elif t.attrs.get('class') and t.attrs.get('class')[0] == "a-price-decimal" and not foundPrice2:
        text = re.sub(r'[^a-zA-Z0-9]', '', t.text)
        if text != "":
            price += (float(text) / 100)
        foundPrice2 = True
print("DONE!")
print("if you see this message for over 1 minute, close this window.")
if price <= targetPrice:
    messagebox.showwarning("Low Price Alert!", f"The price for \"{nameOfItem}\" is: {price}, which is lower than your target price of {targetPrice}! To buy, the link is: {webpage}")
