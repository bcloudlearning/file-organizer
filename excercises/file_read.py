with open ("Goals.txt", "r") as file:
	content = file.read()

print(content) 



## without using "with"  ##

file = open("goals.txt", "r")

content = file.read()

file.close()

print(content)