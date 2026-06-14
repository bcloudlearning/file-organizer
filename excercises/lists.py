clouds = ["AWS", "GCP", "AZURE"]

'''
print(clouds[0])
print(clouds[1])
print(clouds[2])

print(len(clouds))'''

clouds.append("Ctrl-S")

print(clouds)

for cloud in clouds:
	print(cloud)


technologies = [
    "Python",
    "AWS",
    "Docker",
    "Kubernetes"
]

for tech in technologies:
	print(f" I am learning {tech}")

favorite_cloud = input("Enter your favorite cloud provider: ")
technologies.append(favorite_cloud)
print(technologies)
