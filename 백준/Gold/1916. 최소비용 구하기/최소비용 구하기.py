import sys
import heapq

input = sys.stdin.readline

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

# list의 size는 56 dict의 size는 64
# 나중에 blog로 왜 그런지 정리할 것.
graph = [[] for _ in range(n+1)] 

# graph 관계 리스트 생성
# graph[a].append([b, cost]) : a에서 b로 가는데 cost만큼의 비용이 든다.
# a -> b로 가는 경로가 꼭 단일 경로가 아닐수도 있음.
for _ in range(m):
    start_city, end_city, cost = map(int, input().split())
    graph[start_city].append((end_city,cost))

# 출발점의 도시 번호와 도착점의 도시 번호
start_city, end_city = map(int,input().split())
costs = [float("inf") for _ in range(n+1)]
heap = []
costs[start_city] = 0 # 첫 시작점은 cost가 0
# 최저 거리대로 뽑아야 하므로, heap에 정렬되기 원하는 순서대로 넣어줘야 한다.
heapq.heappush(heap,(0, start_city)) 

# update cost
while heap:
    current_cost, current_city = heapq.heappop(heap)

    # costs에 저장된 값보다 비싼 값이면
    # 굳이 그 경로로 갈 필요가 없다.
    if costs[current_city] < current_cost:
        continue

    for next_city, next_cost in graph[current_city]:
        sum_cost = current_cost + next_cost

        if sum_cost < costs[next_city]: 
            costs[next_city] = sum_cost
            heapq.heappush(heap, (sum_cost, next_city))

# end_city에 update된 값을 뽑아주기!
print(costs[end_city])