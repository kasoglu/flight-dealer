# Flight Dealer

A Cheap Flight Alert program sends you a SMS to notify cheap flights (return) in next 6 months.

<p align="center">
  <img src="https://i.ibb.co/k5D0rky/flight-dealer.png" alt="flightdealer"/>
</p>

# Installing
Download the [Python 3](https://python.org) installer package from the official website and install it, if not installed previously.

* Run the following in the terminal to install the Requests module to **post** your working data to [Sheety](https://sheety.co/).
```
pip install requests
```

* Follow to [this](https://docs.google.com/spreadsheets/) link to create a blank **Google Spreadsheets** file to save our data here. (You can also edit my [Google Sheets]() list.)
* Go to the [Tequila Flight Search API Documentation](https://tequila.kiwi.com/portal/docs/tequila_api) website and select **"Get Your API Key"** to sign up for a free account. 
* Once logged in, you should be able to access your ```TEQUILA_API_KEY```. You can replace it in the ```flight_search.py``` file.
* Now, Log into [Sheety](https://sheety.co/) with your Google Account. (Make sure the email matches between your Google Sheet and Sheety Account)
* Click on "New Project" and create a new project in Sheety with the name "Flight Deals" and paste in the URL of your own Google Sheet file.
* Modify the workouts API endpoint and enable GET and POST settings.
* Add either "Bearer Token" to your Sheety endpoint to secure it. 

# How to Use?

Download the source code from the repository and run the file just as any other Python script (.py) file.
```
python3 main.py
```
* Note! For the code to work you need to replace all the placeholders with your own details. e.g. ```TEQUILA_API_KEY```, ```SHEETY_USER_ID```, ```PROJECT_NAME```.

Once you replace the own details in the code, run the program.

It will search all destinations and detect which one is the lowest price and send an SMS alert to your mobile phone.

Check out the link below for more details about API sources.


# Documentations

* [Sheety](https://sheety.co/)
* [Twilio SMS API](https://www.twilio.com/docs/sms)
* [Tequila Flight Search API Documentation](https://tequila.kiwi.com/portal/docs/tequila_api)
* [Google Sheets](https://docs.google.com)

