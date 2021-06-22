import os
import requests
import datetime
from twilio.rest import Client
import json
url = "https://api.openweathermap.org/data/2.5/onecall"
api_id = os.environ.get("API_ID")
print(api_id)
params = {
    "lat": 31.956289,
    "lon": 75.616844,
    "appid": api_id,
    "exclude": "current,minutely,hourly",
    "units": "metric"
}
response = requests.get(url=url, params=params)
data = response.json()
# with open("daily.json", "w") as data_file:
#     json.dump(data, data_file, indent=4)
today_sunrise_time = datetime.datetime.fromtimestamp(data["daily"][0]["sunrise"]).strftime('%H:%M:%S')
today_sunset_time = datetime.datetime.fromtimestamp(data["daily"][0]["sunset"]).strftime('%H:%M:%S')
today_moonrise_time = datetime.datetime.fromtimestamp(data["daily"][0]["moonrise"]).strftime('%H:%M:%S')
today_moonset_time = datetime.datetime.fromtimestamp(data["daily"][0]["moonset"]).strftime('%H:%M:%S')
max_temp = data["daily"][0]["temp"]["max"]
min_temp = data["daily"][0]["temp"]["min"]
weather_condition = data["daily"][0]["weather"][0]["description"]
today_forecast = f"\n\n\n\nsunrise : {today_sunrise_time}\nsunset : {today_sunset_time}\nmoonrise : {today_moonrise_time}\nmoonset : {today_moonset_time}\nmax temp : {max_temp}˚ C\nmin temp : {min_temp}˚ C"
print(today_forecast)
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)
message = client.messages \
                .create(
                     body=today_forecast,
                     from_='+12095536133',
                     to='+919878965313'
                 )
print(message.sid)
