import sys

input = sys.stdin.readline

n, x = map(int,input().split())

arr = list(map(int,input().split()))
acc_visit = sum(arr[:x])
max_visit = acc_visit
max_days = 1

# 슬라이딩 윈도우
for i in range(x,n):
    acc_visit -= arr[i-x]
    acc_visit += arr[i]

    # update
    if max_visit < acc_visit:
        max_visit = acc_visit
        max_days = 1
    elif max_visit == acc_visit:
        max_days += 1

if max_visit != 0:
    print(max_visit,max_days, sep='\n', end='')
else:
    print("SAD")
