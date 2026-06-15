import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

users = response.json()

print(users)

for user in users:
	print(user["name"])  ####   Here users is a List  and user is a dictionary within the list ####


