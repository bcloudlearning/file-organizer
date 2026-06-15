import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

print(response.status_code)
print(response.json())   

'''
import json

data = json.loads(response.text)

  -----or-------

print(response.json()) 

'''


print(type(response.json()))

#print(response.text)
#print(type(response.text))