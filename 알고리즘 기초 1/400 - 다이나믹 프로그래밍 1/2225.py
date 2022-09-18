import sys
n,k = map(int,sys.stdin.readline().split())

case_plus = [[0] * (n+1) for _ in range(k+1)]
case_plus[1] = [1 for _ in range(n+1)]

for i in range(2,k+1):
    for j in range(n+1):
        case_plus[i][j] = sum(case_plus[i-1][:j+1])

print(case_plus[k][n] % 1000000000)