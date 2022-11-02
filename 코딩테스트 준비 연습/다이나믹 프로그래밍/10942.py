from sys import stdin
input = stdin.readline
n = int(input())
arr = list(map(int,input().split()))
m = int(input())
'''
dp[i][j] : i번째 수부터 j번째 수까지가 펠린드롭인지 확인해주는 list
dp[i][i] -> 무조건 펠린드롭
dp[i][i+1] -> arr[i] == arr[i+1] 이라면 무조건 펠린드롭
'''


dp = [[0 for _ in range(n)] for _ in range(n)] 

# dp 초기화
for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1

for length in range(2,n):
    for j in range(n-length):
        if arr[j] == arr[j+length] and dp[j+1][j+length -1]:
            dp[j][j+length] = 1 

for _ in range(m):
    s,e = map(int,input().split())
    print(dp[s-1][e-1])