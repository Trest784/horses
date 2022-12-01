import requests
from pprint import pprint
from confiq_meteo import open_weather_token
from confiq_meteo import token_bot

class Exception:
    pass


def get_weather(city,open_weather_token):
    global ex
    try:
        r = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        print(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["temp"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]

        print(
              f"Погода в городе:{city}\nТемпература:{cur_weather}C\n"
              f"Влажность:{humidity}\nДавление:{pressure} мм.рт.ст\nВетер:{wind}\n"
              f"хорошего дня!"
              )

    except Exception as ex:
        print(ex)
        print("проверьте название города")



def main():
    city = input("Введите город")
    get_weather(city,open_weather_token)





if __name__ == '__main__':
    main()



