import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
solve = [1] * n

for i in range(1,n):
	for j in range(i):
		if a[j] > a[i]:
			solve[i] = max(solve[j] + 1, solve[i])
print(max(solve))