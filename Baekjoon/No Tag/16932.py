import sys
from collections import deque

def grouping(i:int,j:int, category:int):
    q = deque()
    q.append((i,j))
    d = [(0,1), (0,-1), (1,0), (-1,0)] # 인접한 지역을 가도록 그루핑
    count = 1
    arr[i][j] = category
    while q:
        hr, hc = q.popleft()
        for dr, dc in d:
            nr, nc = hr + dr, hc + dc
            if not (0<=nr<n and 0<=nc<m): continue
            if arr[nr][nc] == 1:
                arr[nr][nc] = category
                count += 1
                q.append((nr,nc))
    return count

def max_count(one_group_dict:dict):
    d = [(0,1), (0,-1), (1,0), (-1,0)] # 인접한 지역을 가도록
    max_value = 0
    for i in range(n):
        for j in range(m):
            # 0의 상하좌우를 살피기
            if arr[i][j] == 0:
                count = 1
                category_set = set()
                for dr, dc in d:
                    nr, nc = i + dr, j + dc
                    if not (0<=nr<n and 0<=nc<m): continue
                    if not arr[nr][nc]: continue
                    category_set.add(arr[nr][nc])
                for category in category_set:
                    count += one_group_dict[category]
                max_value = max(max_value, count)
    return max_value

def solution():
    # 그냥 브루트포스 해서 arr[i][j] = 1로 바꾼다음 순회하면 반드시 이미 1로 덧칠된 부분이 중복된다.
    # 따라서, 인접한 1들끼리 범위를 나눠준다.
    category = 2 # 0인지 1인지 구분하기 위해, 그와 전혀 연관없는 2부터 시작
    one_group_dict = dict()
    max_value = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                count = grouping(i,j,category)
                one_group_dict[category] = count
                max_value = max(max_value, count)
                category += 1

    # 0의 상하좌우를 살피기
    zero_max_value = max_count(one_group_dict)
    max_value = max(max_value, zero_max_value)
    return max_value

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_value = solution()
    print(max_value)