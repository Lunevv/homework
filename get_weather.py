import requests

weather_location = ["Лондон", "svo", "Череповец"]

url = "https://wttr.in/{}?nTqM&lang=ru"
url1 = url.format(weather_location[0])
url2 = url.format(weather_location[1])
url3 = url.format(weather_location[2])

response1 = requests.get(url1)
response2 = requests.get(url2)
response3 = requests.get(url3)
response1.raise_for_status()
response2.raise_for_status()
response3.raise_for_status()

print(response1.text)
print(response2.text)
print(response3.text)
