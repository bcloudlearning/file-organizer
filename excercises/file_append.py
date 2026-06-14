with open("career_goals.txt","a") as file:
	file.write("\nappending this text into existing file")

with open("career_goals.txt", "r") as file:
	content = file.read()


print(content)