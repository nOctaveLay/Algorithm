import sys
input = sys.stdin.readline

n = int(input())

input_list = [list(map(int,input().rstrip("\n").split())) for _ in range(n)]

dp = [[0,0,0] for _ in range(n)]

dp[0][0] = input_list[0][0]
dp[0][1] = input_list[0][1]
dp[0][2] = input_list[0][2]

for i in range(n):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + input_list[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + input_list[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + input_list[i][2]

result = min(dp[n-1])
print(result)