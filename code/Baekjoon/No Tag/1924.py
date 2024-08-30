#1924
string = input().split(" ")
x = int(string[0])
y = int(string[1])
for a in range(1,x):
	if (a == 4 or a == 6 or a == 9 or a == 11):
		y += 30
	elif (a == 2):
		y += 28
	else:
		y += 31
obj_y = y % 7
day = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
print(day[obj_y])
