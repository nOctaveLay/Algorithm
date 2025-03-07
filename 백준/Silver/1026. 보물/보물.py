import sys
input=sys.stdin.readline
n=int(input())
arr_A = sorted(list(map(int,input().split())))
arr_B = sorted(list(map(int,input().split())), reverse=True)

result = 0
for i in range(n):
    result += arr_A[i] * arr_B[i]
print(result)