import sys

input = sys.stdin.readline

n = int(input())
INF = 2000000*n

TSC = [[INF for _ in range(1<<n)] for _ in range(n)]
W = [list(map(int,input().split())) for _ in range(n)]

def return_cost(current,visited):
    # 방문이 모두 끝났을 경우 처음으로 돌아오는 비용을 리턴한다.
    if visited == (1<<n) - 1:
        if W[current][0]:
            return W[current][0]
        else:
            return INF

    # 이미 저장된 값이 있다면, 다시 업데이트 할 필요는 없다 (메모이제이션)
    if TSC[current][visited] != INF:
        return TSC[current][visited]

    # 0번째 city는 이미 처음에 출발한 도시이므로, 출발하지 않은 도시들 중에서 세어야 한다.
    
    for city in range(1,n):
        # 방문을 하지 않은 도시이고, 가는 경로가 있다면
        if not W[current][city]: continue
        elif visited & (0b1 << city): continue
        else: TSC[current][visited] = min(TSC[current][visited], return_cost(city,visited | 0b1 << city)+ W[current][city])
    return TSC[current][visited]

print(return_cost(0,1),end = '')