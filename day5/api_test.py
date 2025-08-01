import requests

my_url = "https://dummyjson.com/users"

response = requests.get(url=my_url)
data = response.json()
print(data["users"][0]["username"])