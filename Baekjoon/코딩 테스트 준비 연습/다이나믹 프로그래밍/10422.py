import sys
input = sys.stdin.readline
# dp[i] : 길이가 i 일 때 올바른 괄호의 갯수.
# 올바른 괄호 안에 올바른 괄호가 들어가더라도 그것은 올바른 괄호이다.
# dp[i] = (올바른 괄호들의 경우의 수) 나머지 올바른 괄호들의 경우의 수

# 전체 길이가 i 이므로, (올바른 괄호의 경우의 수) 의 길이를 j라 할 때
# 나머지 올바른 괄호들의 길이는 i-j가 된다.
# 또한, () 안에 올바른 괄호의 경우의 수를 넣으므로, j-2의 길이를 갖게 된다.
# 즉 dp[i] = (dp[j-2]) dp[i-j]

T = int(input())
max_value = 5001
dp = [0 for _ in range(max_value)]
dp[0] = 1
dp[1] = 0
dp[2] = 1

# dp 초기화
# 
for i in range(3,max_value):
    for j in range(2,i+1):
        dp[i] += dp[j-2] * dp[i-j]
    dp[i] %= 1000000007

for _ in range(T):
    l = int(input())
    print(dp[l])