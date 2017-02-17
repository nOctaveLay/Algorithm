list_Eng = [chr(x) for x in range(97,123)]
list_result = [0 for _ in range(97,123)]
input_string = input().lower()
for x in input_string:
	position = list_Eng.index(x)
	list_result[position] += 1
max_num = max(list_result)
count = 0
for x in range(len(list_result)):
	if list_result[x] == max_num:
		count += 1
if count > 1:
	print("?")
else:
	print(list_Eng[list_result.index(max_num)].capitalize())