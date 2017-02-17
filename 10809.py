list_Eng = [chr(x) for x in range(97,123)]
list_result = [-1 for _ in range(97,123)]
input_string = input()
for i in range(len(input_string)):
	position = list_Eng.index(input_string[i])
	if (list_result[position] == -1):
		list_result[position] = i
for x in list_result:
	print(x,end=' ')
print()