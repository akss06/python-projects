import requests
from plyer import notification
import time


country = input("Choose a country to view its aqi: ")

if country.upper() == 'INDIA':
    latitude = 15.491997
    longitude = 73.81800065

elif country.upper() == 'AUSTRALIA':
    latitude = -33
    longitude = 151

elif country.upper() == 'CANADA':
    latitude = 50
    longitude = -96

elif country.upper() == 'PAKISTAN':
    latitude = 30
    longitude = 69

elif country.upper() == 'JAPAN':
    latitude = 36
    longitude = 138

elif country.upper() == 'CHINA':
    latitude = 35
    longitude = 104

elif country.upper() == 'KOREA':
    latitude = 35
    longitude = 127

elif country.upper() == 'USA':
    latitude = 37
    longitude = 95

elif country.upper() == "UK":
    latitude = 55
    longitude = 3

elif country.upper() == "SRI LANKA":
    latitude = 7
    longitude = 80

url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={latitude}&lon={longitude}&appid=9d9a6d59683efa93aad223bae15bc140"       #api = 9d9a6d59683efa93aad223bae15bc140
response = requests.get(url)                 



list1 = response.json()['list']
aqi = list1[0]['main'].values()

for i in aqi:
    aqi = i


if aqi == 1:
    mess = "Air quality is satisfactory, and air pollution poses little or no risk."

elif aqi == 2:
    mess = "Air quality is acceptable. However, there may be a risk for some people."

elif aqi == 3:
    mess = "Members of sensitive groups may experience health effects. The general public is less likely to be affected."

elif aqi == 4:
    mess = "Some members of the general public may experience health effects."

elif aqi == 5:
    mess = "Health alert: The risk of health effects is increased for everyone."



while True:     

    notification.notify(
        title = f"CURRENT AQI OF {country.upper()} \U0001F637",
        message = f"AQI IS {aqi}:\n{mess}",
        app_icon = "F:/icons8-air-quality-64.ico",
        timeout = 7

    )


    time.sleep(10)   
