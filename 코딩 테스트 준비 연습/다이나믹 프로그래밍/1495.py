import sys
input = sys.stdin.readline

n, s, m = map(int,input().split())
v = list(map(int,input().split()))
dp = [[0 for _ in range(m+1)] for _ in range(n+1)] # i번째 곡을 연주할 때 Volume이 j 이다. 이 때 이 Volume이 가능한지 T/F
dp[0][s] = True # 연주하지도 않았을 때의 초기값

for i in range(1,n+1): # 곡의 갯수
    for j in range(0,m+1): # Volume 값.
        if dp[i-1][j]: # 이전의 곡을 연주할 때의 Volume이 j였을 때, 이 Volume이 가능했다면,
            # 범위 check
            if j - v[i-1] >= 0:
                dp[i][j-v[i-1]] = True
            if j + v[i-1] <= m:
                dp[i][j+v[i-1]] = True

for j in reversed(range(m+1)):
    if dp[n][j]:
        print(j,end='')
        exit()
print(-1,end='')