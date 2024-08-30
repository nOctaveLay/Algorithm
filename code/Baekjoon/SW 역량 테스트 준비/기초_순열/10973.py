import sys
n = int(sys.stdin.readline())
permutation_list = sys.stdin.readline().rstrip("\n").split(" ")

for i in range(n):
	permutation_list[i] = int(permutation_list[i])

find = False
for i in range(n-2,-1,-1):
	# 오른차순일 경우
	if permutation_list[i] > permutation_list[i+1]:
		for j in range(n-1,0,-1):
			if permutation_list[i] > permutation_list[j]:
				permutation_list[i],permutation_list[j] = permutation_list[j],permutation_list[i]
				permutation_list = permutation_list[:i+1] + sorted(permutation_list[i+1:],reverse=True)
				find = True
				break
	if find:
		print(*permutation_list)
		break
if not find:
	print(-1)