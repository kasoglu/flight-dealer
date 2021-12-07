import requests

#Replace below 👇 area with your informations as a String.
SHEETY_USER_ID = YOUR SHEETY USER ID
PROJECT_NAME = YOUR PROJECT NAME
SHEET_NAME = YOUR SHEET NAME
#Replace above 👆 area with your informations as a String.

SHEETY_PRICES_ENDPOINT = f"https://api.sheety.co/{SHEETY_USER_ID}/{PROJECT_NAME}/{SHEET_NAME}"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
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
                json=new_data
            )
            print(response.text)
