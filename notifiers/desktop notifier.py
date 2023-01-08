import requests
from plyer import notification
import time

url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=73598f6aa8e34deb8166d47748909b3f'  #apiKey=73598f6aa8e34deb8166d47748909b3f

response = requests.get(url)

response_json = response.json()

for i in response_json["articles"]:
            notif = i["title"]


            notification.notify(
                title = "TOP HEADLINES TODAY \U0001F4F0",
                message = notif,
                app_icon = "F:/icons8-us-news-64.ico",
                timeout = 7
            )
        
            time.sleep(1)
