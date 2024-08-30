in_n = int(input())
result = ''
for _ in range(in_n):
	in_list = input().split(" ")
	repeat = in_list[0]
	re_string = in_list[1]
	for x in in_list[1]:
		for y in range(int(repeat)):
			result += x
	print(result)
	result = ''