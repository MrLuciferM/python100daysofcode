from twilio.rest import Client
from private import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, MY_NUMBER, TWILIO_NUMBER


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        Message = self.client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER,
        )
        # Prints if successfully sent.
        print(Message.sid)
