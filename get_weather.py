import requests


WEATHER_LOCATION = ["Лондон", "svo", "Череповец"]
weather_url = "https://wttr.in/{}"
paylad = {"nTqM": "", "lang": "ru"}


def get_weather(city: str):
    url = weather_url.format(city)
    response = requests.get(url, params=paylad)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    for location in WEATHER_LOCATION:
        print(get_weather(location))
