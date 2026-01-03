import sys

input = sys.stdin.readline


n, k = map(int,input().split()) # 국가는 1<=k<=n

arr = [list(map(int,input().split())) for i in range(n)]

# 실전에서 속지 말 것
# 각 국가를 나타내는 정수 + 금, 은, 동메달의 개수임

arr.sort(key=lambda x:(-x[1], -x[2], -x[3]))
for i in range(n-1,-1,-1):
    if arr[i][0] == k:
        # 같은 매달일 때 순위가 낮아짐
        while i > 0 and arr[i][1:] == arr[i-1][1:]:
            i -=1
        print(i+1)
        exit()
if i == 0:
    print(1)