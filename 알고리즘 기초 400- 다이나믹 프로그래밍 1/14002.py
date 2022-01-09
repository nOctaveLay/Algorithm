import sys
input = sys.stdin.readline
n = int(input())
seq =  list(map(int,input().split()))
dp = [[x] for x in seq]

for i in range(n):
    for j in range(i):
        if seq[i] > seq[j] and len(dp[j]) + 1 > len(dp[i]):
                dp[i] = dp[j] + [seq[i]]
max_num = 0
max_list = []
for i in dp:
    if max_num < len(i):
        max_num = len(i)
        max_list = i
print(max_num)
print(*max_list)