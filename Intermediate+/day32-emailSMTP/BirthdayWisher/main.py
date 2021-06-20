##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import pandas as pd
import random
import smtplib
from INFO import MY_EMAIL, PASSWORD

now = dt.datetime.now()

birthdays = pd.read_csv('birthdays.csv')
birthdays_today = birthdays.loc[(birthdays.month == now.month) & (birthdays.day == now.day)]
# print(birthdays_today)

for index, row in birthdays_today.iterrows():
    template_file = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(template_file) as file:
        letter_template = file.read()
    person_name = row["name"]
    person_email = row["email"]
    letter = letter_template.replace("[NAME]", person_name)
    print(letter)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person_email,
            msg=f"Subject: Happy Birthday\n\n{letter}"
        )
