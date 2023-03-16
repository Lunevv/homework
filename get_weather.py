import requests

weather_location = ["Лондон", "svo", "Череповец"]
url_weather = "https://wttr.in/{}"
paylad = {"nTqM": "", "lang": "ru"}

def get_weather():
    for location in weather_location:
        url = url_weather.format(location)
        response = requests.get(url, params=paylad)
        response.raise_for_status()
        print(response.text)
    return
if __name__ == '__main__':
    get_weather()
