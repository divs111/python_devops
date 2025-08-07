import requests

weather_url = "https://api.openweathermap.org/data/2.5/weather?q=Pune&appid=ed33c36a892c914a540fe536089233b2"

response = requests.get(weather_url)
data = response.json()
#print(dir(response))
#print(response.status_code.__doc__)
print(data)

if response.status_code == 200:
    print(f"weather in Pune : {data['weather'][0]['description']}")
else:
    print(f"Error : {data.get('message','unable to fetch data')}")