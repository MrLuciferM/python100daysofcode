from twilio.rest import Client
from private import MY_EMAIL, PASSWORD
import smtplib

class NotificationManager:

    def send_emails(self, emails,names, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            for i in range(len(emails)):
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=emails[i],
                    msg=f"Subject:New Low Price Flight!\n\nHey {names[i]},\n{message}\n{google_flight_link}".encode('utf-8')
                )

