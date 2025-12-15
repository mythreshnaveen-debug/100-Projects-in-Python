# Project 38 - Workout Tracker
# This uses a simple Generative AI to get the data out of a basic, human text.
# Then, it sends it to 'Sheety' to send it to a spreadsheet.

from datetime import datetime
import requests, os


#Get Data

print("BASIC INFO:")
GENDER = input("Gender: ")
WEIGHT_KG = input("Weight (in kg): ")
HEIGHT_CM = input("Height (in cm): ")
AGE = input("Age: ")

endpoint = os.environ["Proj38-apiKey"]
headers = {
    'x-app-id': os.environ.get("Proj38-xAppId"),
    'x-app-key': os.environ.get("Proj38-xAppKey")
}

body = {
    "query": input("Please enter what workout you did, and how much times you did it. (Saying for how long, is also a bonus.)\n\nFor multiple workouts: Only say 1 workout in the query panel, and restart the program for the other ones.\n\n\n>"),
    "gender": GENDER.lower(),
    "weight_kg": float(WEIGHT_KG),
    "height_cm": float(HEIGHT_CM),
    "age": float(AGE)
}

response = requests.post(url=endpoint, json=body, headers=headers)
data = response.json()
now = datetime.now()

minutes = str(data["exercises"][0]["duration_min"]) + " minutes"
title = data["exercises"][0]["name"]
calories = data["exercises"][0]["nf_calories"]
time = datetime.now().strftime("%X")
date = f"{now.month}/{now.day}/{now.year}"
print(f"EXTRACTED DATA. (Name:{title})")
print(f"This took you: {minutes}.")
print(f"Calories: {calories}")


# Post Data
endpoint = os.environ.get("Proj38-sheetyEndpoint")

body = {
    "workout": {
        "date": date,
        "time": now.strftime("%X"),
        "exercise": title,
        "duration": minutes,
        "calories": calories
    }
}

print("Saving..")

response = requests.post(url=endpoint, json=body, auth=(os.environ.get("Proj38-sheetyUser"), os.environ.get("Proj38-sheetyPass")))
data = response.json()
print("Saved! You may exit this app.")
