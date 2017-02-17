list_ENG = [chr(x) for x in range(65,90+1)]
list_sec = []
count,sec = 0,2
count_sec = 1
while count < len(list_ENG)-2:
	list_sec.append(sec)
	if count_sec == 3:
		count_sec = 0
		if sec == 7 or sec == 9:
			list_sec.append(sec)
		sec +=1
	count += 1
	count_sec += 1
input_string = input()
result = 0
for x in input_string:
	position = list_ENG.index(x)
	result += list_sec[position]+1
print(result)