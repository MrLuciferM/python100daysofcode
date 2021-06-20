import smtplib
import datetime as dt
import random
from INFO import MY_EMAIL, PASSWORD, RECEIVER_EMAIL

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes).strip()
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )

    print(quote)