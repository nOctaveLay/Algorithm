# 복습 필요

from itertools import accumulate
from sys import stdin
input = stdin.readline
t = int(input())
for _ in range(t):
    k = int(input())
    arr = list(map(int,input().split()))
    sums = list(accumulate(arr))
    
    dp = [[0 for _ in range(k)] for _ in range(k)]

    for i in range(k-1): #자신과 그 옆을 합할때 (len = 1)
        dp[i][i+1] = arr[i] + arr[i+1]

    for j in range(2, k): # len >= 2
        i = 0
        while i+j < k:
            for mid in range(i,i+j):
                partial_sum = sums[i+j] - sums[i-1] if i > 0 else sums[i+j]
                if dp[i][i+j]:
                    dp[i][i+j] = min(dp[i][i+j], dp[i][mid] + dp[mid+1][i+j] + partial_sum)
                else:
                    dp[i][i+j] = dp[i][mid] + dp[mid+1][i+j] + partial_sum
            i += 1

    print(dp[0][-1])