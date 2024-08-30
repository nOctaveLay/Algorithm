import sys
n = int(sys.stdin.readline())
set_num = [i for i in range(1,n+1)]

def set_permutation(permutation_list):
	for i in range(n):
		permutation_list[i] = int(permutation_list[i])

	for i in range(n-2,-1,-1):
		# 오른차순일 경우
		if permutation_list[i] < permutation_list[i+1]:
			for j in range(n-1,0,-1):
				if permutation_list[i] < permutation_list[j]:
					permutation_list[i],permutation_list[j] = permutation_list[j],permutation_list[i]
					permutation_list = permutation_list[:i+1] + sorted(permutation_list[i+1:])
					return permutation_list
	return 0

	
while True:
	if set_num == 0 : break
	else : 
		print(*set_num)
		set_num = set_permutation(set_num)