import requests

def get_users():
	response = requests.get("https://jsonplaceholder.typicode.com/users")
	print(response.status_code)
	
	if response.status_code == 200:
		#users = response.json()
		print("response_json type is: ",type(response.json()))
		return response.json()
		
	else:
		print("Something is Wrong")	
		return None





def generate_report(users):
	report = "User List \n\n"
	for user in users:
		report += f"id:{user['id']}\n"
		report += f"name:{user['name']}\n"
		report += f"email:{user['email']}\n\n"
	print("report type is:" ,type(report))
	return report
	



def save_userreport(report):
	with open("generated_user_report.txt", "w") as file:
		file.write(report)
	print("report saved successfully")


users = get_users()
user_report = generate_report(users)
save_userreport(user_report)

		