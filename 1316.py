in_num = int(input())
list_Eng = [chr(x) for x in range(97,123)]
list_Res = [0 for _ in range(97,123)]
result = 0
for _ in range(in_num):
	string = input()
	i,count = 0,0
	while i <  len(string):
		Res_position = list_Eng.index(string[i])
		if list_Res[Res_position] >0 and string[i] != string[i-1]:
			count += 1
		else:
			list_Res[Res_position] += 1
		i += 1
	if count == 0:
		result += 1
	list_Res = [0 for _ in range(97,123)]
print(result)