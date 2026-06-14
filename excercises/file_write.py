with open("career_goals.txt","w") as file:
	file.write("This is writing into text file")

with open("career_goals.txt", "r") as file:
	content = file.read()


print(content)