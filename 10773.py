num = int(input())
list_for_result = []
for _ in range(num):
	input_num = int(input())
	if input_num == 0:
		list_for_result.pop()
	else:
		list_for_result.append(input_num)
print(sum(list_for_result))