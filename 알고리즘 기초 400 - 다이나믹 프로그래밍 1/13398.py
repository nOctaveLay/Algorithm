import sys
input = sys.stdin.readline
n = int(input())
input_arr = list(map(int,input().split()))
dp = [[0,0] for _ in range(n)]

dp[0][0] = input_arr[0] #제거를 안 했을 경우
dp[0][1] = 0 #제거했을 경우

ans = -10**8 if n > 1 else dp[0][0]
for i in range(1,n):
    #제거하지 않았을 경우
    dp[i][0] = max(dp[i-1][0]+input_arr[i],input_arr[i])

    #제거했을 경우
    dp[i][1] = max(dp[i-1][1]+input_arr[i],dp[i-1][0])

    ans = max(ans,dp[i][0],dp[i][1])
print(ans,end = '')