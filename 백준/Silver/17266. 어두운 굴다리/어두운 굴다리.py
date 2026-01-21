import sys

input = sys.stdin.readline

n = int(input()) # 총 거리 길이
m = int(input()) # 가로등 개수

# 0- 첫 가로등 위치
# 가로등과 가로등 사이
# 마지막 가로등 위치 - 끝 가로등 위치

l = list(map(int,input().split()))
max_distance = l[0] # 0 ~ 첫 가로등 위치까지의 거리

for i in range(m-1):
    max_distance = max((l[i+1] - l[i])//2+(l[i+1] - l[i])%2,max_distance)

# 마지막 가로등 위치 - 끝 가로등 위치
max_distance = max(n-l[-1],max_distance)
print(max_distance)