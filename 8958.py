n_s = int(input())
list_s = []
for _ in range(n_s):
	input_s = input()
	count = 0
	result = 1

	#최종 result는 result_O 이다.
	result_O = 0
	while count < len(input_s):
		if input_s[count] == "O" :
			if input_s[count-1] == "X":
			#"O"전에 "X"가 나오면 result = 1로 초기화 되어야 한다.
				result = 1
			#"O"다음에 "O"가 나오면 계속 값이 더해져야 한다.		
			if input_s[count] == input_s[count-1] and count >0:
				result += 1
			result_O += result
		else:
			result = 0
		count += 1
	print(result_O)
