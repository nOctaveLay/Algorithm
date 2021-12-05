in_list = input().split(" ")
temp = ''
result = []
for x in in_list:
	for y in x:
		temp = y + temp
	result.append(int(temp))
	temp = ''
print(max(result))