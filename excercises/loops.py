'''#exercise 1
for i in range(1,6):
    print(f"Day {i}") '''


days = int(input("Eneter number of days you will study:"))
# i = 0  ==> is unnecessary because the for loop creates and updates i automatically.
for i in range(1,days+1):
	print(f"study day {i}")