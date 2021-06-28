import requests
from private import BEARER

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/7e71ed13f385fb86dd4416dea0eb2f08/flightDealsAlert/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/7e71ed13f385fb86dd4416dea0eb2f08/flightDealsAlert/users"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.__header = {
            "Authorization": BEARER
        }
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.__header)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.__header
            )
            # print(response.text)

    def add_user_data(self,new_user):
        response = requests.post(url=SHEETY_USERS_ENDPOINT, json = new_user, headers=self.__header)
        print(response.text)

    def ask_user_details(self):
        print("Welcome to Kunal's Flight Club.\n"
            "We find the best flight deals and email you.")

        first_name = input("What is your first name?")
        last_name = input("What is your last name?")
        email = input("What is your email?")
        email_confirmation = input("Type your email again.")

        if email.lower() == email_confirmation.lower():
            new_user = {
                "user": {
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email
                }
            }
            self.add_user_data(new_user)
            print("You're in the club!")
        else:
            print("Sorry, The emails doesn't match. Please try again!")

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT,headers=self.__header)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data