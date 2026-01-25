# brute-force로 풀기엔 너무 양이 많음..
# 어떤 값 x를 찾고, 그에 맞는 걸 범주 내에서 찾아야 한다고 하자..
# 뭘 쓸 수 있지?? 탐색법을 쓰자

import sys

input = sys.stdin.readline

answer = 0 # 총 예산들 중 최대값인 정수
n = int(input()) # 예산들
arr = list(map(int,input().split()))
m = int(input()) # 총 예산

low, high = 0, max(arr) # 예산들 사이에서 어떤 값 x를 찾고, 이 값들을 전부 더해 총 예산에 부합하는지 확인

while low <= high: #low값이 high에 도달하면, 전 범위를 탐색한 것과 같다.
    total = 0
    
    mid = (low+high) // 2 # 예산의 최대치를 범주의 중간값으로 설정

    # 예산의 최대치보다 넘으면 예산의 최대치를 제공
    # 그렇지 않을 경우 그 금액을 제공
    # 즉, 예산과 금액의 min값을 제공
    for x in arr:
        total += min(x,mid)

    # 계산한 total이 예산을 초과하지 않는가?
    if total <= m:
        low = mid+1 
        answer = mid
    else: #예산을 초과한다면
        high = mid-1 
# low == high 인 지점이면 전 범위를 탐색한 것이므로
print(answer)