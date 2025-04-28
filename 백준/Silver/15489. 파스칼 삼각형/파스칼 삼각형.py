import sys

input=sys.stdin.readline

r,c,w= map(int,input().split())

arr = [[0]*31 for _ in range(31)] #30x30 arr

# field 초기화
for i in range(1,31):
    arr[i][1] = 1
    arr[i][i] = 1

# field 채우기
for i in range(2,31):
    for j in range(1,i):
        if arr[i][j] != 1:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
# 합 계산하기
result = 0
k = 1
for arr_r in range(r,r+w):
    for arr_c in range(c,c+k):
        result += arr[arr_r][arr_c]
    k += 1
print(result)