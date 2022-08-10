import requests
from cfg import weather_token
from pprint import pprint
import datetime
def get_weather(city,weather_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric"

        )
        data = r.json()
        #pprint(data)

        city = data["name"]
        temp = data["main"]["temp"]
        temp_max = data["main"]["temp_max"]
        temp_min = data["main"]["temp_min"]
        Weather = data["weather"][0]["main"]

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе: {city}\nТемпература: {temp}C°\n"
              f"Максимальная температура: {temp_max} \nМинимальная температура: {temp_min}\n"
              f"Состояние погоды: {Weather}\n"
              f"Хорошего дня!"
              )

    except Exception as ex:
        print(ex)
        print("Введите название города верно")

def main():
    city = input("Введите город: ")
    get_weather(city,weather_token)

main()