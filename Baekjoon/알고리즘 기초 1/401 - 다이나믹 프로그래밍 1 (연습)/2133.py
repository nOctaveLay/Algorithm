import sys
input = sys.stdin.readline
dp = [0] * 31
dp[0:3] = [1,0,3]

def count(N):
    if N % 2 != 0: return 0
    else:
        for i in range(4,N+2,2):
            dp[i] = dp[i-2] * 3
            for j in range(4,i+1,2):
                dp[i] += dp[i-j] * 2

    return dp[N]

print(count(int(input())),end = '')