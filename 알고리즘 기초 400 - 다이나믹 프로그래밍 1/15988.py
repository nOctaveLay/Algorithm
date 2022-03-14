import sys
input = sys.stdin.readline
MODULER = 1000000009
test_num = int(input())
dp = [0] * (10 ** 6 + 2)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,10**6+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MODULER

for _ in range(test_num):
    n = int(input())
    sys.stdout.write(str(dp[n]) + '\n')