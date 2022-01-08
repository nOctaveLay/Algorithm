import sys
input = sys.stdin.readline
n = int(input())
seq =  list(map(int,input().split()))

dp = [1] * n
for i in range(n):
    max_value = seq[i]
    for j in range(i):
        if max_value > seq[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))