import sys
input = sys.stdin.readline

N = int(input())
t_list = list()
p_list = list()
dp = list()

for _ in range(N):
    t,p = map(int,input().split())
    t_list.append(t)
    p_list.append(p)
    dp.append(p)
dp.append(0)
for i in reversed(range(N)):
    if t_list[i] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1],p_list[i] + dp[i+t_list[i]])
print(dp[0])