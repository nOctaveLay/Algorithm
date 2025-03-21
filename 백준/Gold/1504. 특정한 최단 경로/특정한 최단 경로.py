import sys
import heapq
input=sys.stdin.readline

n,e=map(int,input().split())

graph=[[] for _ in range(n+1)] # graph[n1]=[(n2,cost)] n1-n2 의 cost를 나타내는 표현.

# graph 초기화 (인접 리스트 이용)
for _ in range(e):
    n1, n2, cost = map(int,input().split())
    # 양방향 길이므로 각자 추가
    graph[n1].append((n2, cost))
    graph[n2].append((n1, cost))

# 반드시 거쳐야 하는 경로 초기화
v1, v2 = map(int,input().split())

def dijkstra(start, end):
    # start부터 시작해 i 까지 가는데 드는 최소 비용 초기화
    min_cost = [float("inf") for _ in range(n+1)]
    min_cost[start] = 0
    q = []

    # python의 heap은 맨 앞의 element를 기준으로 최소 힙임
    # 최소 cost가 드는 방향으로 선택해야 하므로, cost를 앞에 세움
    heapq.heappush(q, (0, start))

    while q:
        current_cost, current_node = heapq.heappop(q)

        # min_cost 부터 시작하지 않는다면 다른 element를 가져오게 함
        if current_cost > min_cost[current_node]: continue

        # min_cost에서 시작하는 거라면 다음 node를 선택
        for adj_node, adj_cost in graph[current_node]:
            next_cost = min_cost[current_node] + adj_cost

            if next_cost < min_cost[adj_node]:
                min_cost[adj_node] = next_cost
                heapq.heappush(q,(next_cost,adj_node))

    return min_cost[end]

# 두 정점을 반드시 지나야 하는 경우
route1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n) # start -> v1 -> v2 -> end
route2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n) # start -> v2 -> v1 -> end

if route1 == float("inf") and route2 == float("inf"): print(-1)
else: print(min(route1, route2))
