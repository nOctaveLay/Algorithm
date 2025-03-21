import sys
import heapq
input=sys.stdin.readline

v,e = map(int,input().split())
start = int(input())
graph = [[] for _ in range(v+1)]

# graph 초기화
for _ in range(e):
    n1,n2,cost = map(int, input().split())
    graph[n1].append((n2,cost))

def dij(start):
    min_value = [float("inf") for _ in range(v+1)] # 편하게 쓰기 위함
    q = [] 
    min_value[start] = 0
    heapq.heappush(q,(0, start))

    while q:
        current_cost, current_node = heapq.heappop(q)
        
        # 최소 value에서 시작하지 않을 경우 -> 스킵
        if current_cost > min_value[current_node]: continue

        # 시작할 경우
        for next_node, next_cost in graph[current_node]:
            sum_cost = min_value[current_node] + next_cost
            if sum_cost < min_value[next_node]:
                min_value[next_node] = sum_cost
                heapq.heappush(q,(sum_cost, next_node))
    return min_value

min_values = dij(start)[1:]
for min_value in min_values:
    if min_value != float("inf"):   
        print(min_value)
    else:
        print("INF")
