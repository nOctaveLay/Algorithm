import sys
import heapq
input=sys.stdin.readline


# 초기 조건 생성
n,e = map(int,input().split())

node = [[] for _ in range(n+1)]

# 인접 리스트를 통해 양방향 그래프 생성 
for _ in range(e):
    a, b, cost = map(int, input().split())
    node[a].append((b, cost))
    node[b].append((a, cost))

# 간선 v1, v2
v1, v2 = map(int,input().split())

def dijkstra(start, end):
    route = [float("inf")] * (n+1)
    
    # 초기 상태
    route[start] = 0

    q = []
    heapq.heappush(q, (0, start)) # cost가 작은 쪽으로 이동해야 하므로, cost를 먼저 씀

    while q:
        current_cost, current_pos = heapq.heappop(q)

        # 만약 저장되어 있는 길이 현재 비용보다 적다면 update 할 필요가 없음
        if route[current_pos] < current_cost:
            continue

        for adj_pos, adj_cost in node[current_pos]:
            sum_cost = route[current_pos] + adj_cost

            # 갱신
            if sum_cost < route[adj_pos]:
                route[adj_pos] = sum_cost
                heapq.heappush(q, (adj_cost, adj_pos))

    return route[end]

route1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
route2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

if route1 == float("inf") and route2 == float("inf"):
    print(-1)
else:
    print(min(route1, route2))