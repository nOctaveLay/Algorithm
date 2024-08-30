'''
0-1 Knapsack 문제.
dp[i][j] = 배낭에 현재 j만큼의 무게로 가득 차 있고, 현재 가치 판단을 해줘야 할 가방이 i번째 일 때의 Value(가치).
'''
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int,input().split())
    W, V = list(), list()
    for _ in range(n):
        w,v = map(int,input().split())
        W.append(w)
        V.append(v)
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,k+1):
            if j - W[i-1] >= 0: dp[i][j] = max(dp[i-1][j], dp[i-1][j-W[i-1]] + V[i-1])
            else: dp[i][j] = dp[i-1][j]
    print(dp[n][k])