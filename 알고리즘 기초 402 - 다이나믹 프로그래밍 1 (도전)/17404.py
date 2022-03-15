'''
RGB 거리에는 집이 N개 있다.
거리는 선분으로 나타낼 수 있고, 1번 집부터 N번집이 순서대로 있다.
집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다.
각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 
아래 규칙을 모두 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해라.

- 1번 집의 색은 2번집, N번집의 색과 같지 않아야 한다.
- N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
- i(2<=i<=N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.


핵심은 infinite를 이용하여 쓰지 않는 것을 닫아두는 것이었다.
'''

n = int(input())
# color_cost[i][j] : i+1번째의 집을 j번째 색으로 칠하는 비용.
color_cost = [list(map(int,input().rstrip("\n").split(" "))) for _ in range(n)]

# i번째 집을 j로 칠할 때 드는 최소 비용
minimum_dp = [[0,0,0] for _ in range(n)]

# 초기 조건
INF = 2000 * n
R,G,B = 0,1,2
answer = INF

for first in range(3):
    
    minimum_dp[0] = [INF,INF,INF]
    minimum_dp[0][first] = color_cost[0][first]

    # 일반 조건 - 3번집 ~ n번집
    for i in range(1,n):
        minimum_dp[i][R] = min(minimum_dp[i-1][B], minimum_dp[i-1][G]) + color_cost[i][R]
        minimum_dp[i][G] = min(minimum_dp[i-1][B], minimum_dp[i-1][R]) + color_cost[i][G]
        minimum_dp[i][B] = min(minimum_dp[i-1][G], minimum_dp[i-1][R]) + color_cost[i][B]

    for i in range(3):
        if first != i: answer = min(answer,minimum_dp[n-1][i])

print(answer,end='')