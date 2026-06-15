import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

data = response.json()

print(type(data))
print(len(data))
print(data)   
