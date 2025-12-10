# Day 32 - Clock
# In this module, we learned how to use the 'datetime' function.
# I actually made the idea for this project, as I couldn't get a SMTP provider to do the original "Email Sender" project that I was supposed to do to work.

import tkinter as tk
from datetime import datetime

# ---------------------- Helpers ---------------------- # (AI helped out with the formatting for this and stuff)

def get_day_suffix(day):
    if 11 <= day <= 13:
        return "th"
    last_digit = day % 10
    if last_digit == 1:
        return "st"
    elif last_digit == 2:
        return "nd"
    elif last_digit == 3:
        return "rd"
    else:
        return "th"

def get_formatted_date():
    now = datetime.now()
    weekday = now.strftime("%A")
    month = now.strftime("%B")
    day = now.day
    year = now.year
    suffix = get_day_suffix(day)
    return f"Today is: {weekday} {month} {day}{suffix}, {year}"

# ---------------------- UI Setup ---------------------- #

root = tk.Tk()
root.title("Clock")

root.geometry("500x200")
root.config(bg="#222831")

# Date label
date_label = tk.Label(
    root,
    text=get_formatted_date(),
    font=("Arial", 16),
    bg="#222831",
    fg="#EEEEEE"
)
date_label.pack(pady=20)

# Time label (big)
time_label = tk.Label(
    root,
    text="00:00:00",
    font=("Arial", 44, "bold"),
    bg="#222831",
    fg="#00ADB5"
)
time_label.pack(pady=10)

# ---------------------- Update Loop ---------------------- #

def format_string(i):
    if i < 10:
        return "0" + str(i)
    else:
        return str(i)

def update_time():
    now = datetime.now()
    # Update time
    time_str = now.strftime("%H:%M:%S")

    if now.hour > 12:
        time_str = f"{format_string(now.hour - 12)}:{format_string(now.minute)}:{format_string(now.second)}" + " PM"
    else:
        time_str += " AM"

    time_label.config(text=time_str)

    date_label.config(text=get_formatted_date())

    root.after(1000, update_time)

update_time()
root.mainloop()
