in_student = int(input())
while (in_student > 0):
	in_student -= 1
	pass_student = 0
	string = input().split(" ")
	string = string[1:]
	sum_sub = 0
	for x in string:
		sum_sub += int(x)
	aver = sum_sub / len(string)
	for x in string:
		if int(x) > aver:
			pass_student += 1
	perc_student = pass_student/len(string) * 100
	print("%0.3f"%perc_student+"%")