# Project 9 - Blind Auction
# Going forward, all logos were usually a part of a separate python file, and was merged for GitHub convenience.
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
data = {}
while True:
    name = input("What is your name?\n")
    price = input("What is the price you are willing to pay?\n")
    bidders = input("Are there any other bidders? (Type 'yes' if there are, type 'no' if there aren't)\n")
    data[name] = int(price)
    if bidders == 'no':
        break
    print("\n\n\n" * 100)
print("THE AUCTION HAS CLOSED!")
greatestPrice = -100
greatestName = ""
for name in data:
    if data[name] > greatestPrice:
        greatestPrice = data[name]
        greatestName = name
print(f"The winner is {greatestName} with a bid of ${greatestPrice}!")
