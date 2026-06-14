import json

family = { "father" : "Bharath", "Mother":"Naomi", "Son":"Vrontis" }

print(family)
print(type(family))


## Converting Dictionary to JSON  ##

json_data = json.dumps(family)

print(json_data)
print(type(json_data))


## Converting json to dictionary  ##

# now json_data contains json text , need to covert it to dictionary

data = json.loads(json_data)

print(type(data))
print(data)
print(data["father"])
