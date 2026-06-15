import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/99")


print(response.status_code)

if response.status_code == 200:
	data = response.json()
	print(data["name"])

else:
	print("Something is wrong")  
