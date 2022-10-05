import sys
from collections import deque
input = sys.stdin.readline

def dfs():
    n = int(input())                                        # 노드의 개수를 입력받는다.
    graph = [[] for _ in range(n+1)]                        # 양방향 그래프를 저장할 리스트다.

    for _ in range(n-1):                                    # n-1개의 간선에 대한 정보를 입력받는다.
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    result = deque(list(map(int, input().split())))         # dfs 탐색 결과를 입력받는다.
    visited = [True] + [False for _ in range(n)]            # 방문 여부를 확인해줄 리스트다.

    stack = []                                              # stack을 생성하고 출발점인 1을 추가한다.
    stack.append(1)                                         

    if result.popleft() != 1:                                 # 첫 번째 원소가 1이 아니라면 0을 출력하고 함수를 종료한다.
        print(0)
        return
    visited[1] = True                                       # 1을 방문처리한다.

    while len(stack) > 0:                                   # stack의 길이가 0이 아닐 때까지 반복한다.
        now = stack.pop()                                   # stack의 원소 하나를 꺼낸다.
        next_node = []                                      # 다음에 이동할 수 있는 노드들을 저장할 리스트다.                            
        for i in graph[now]:                                # 현재 노드와 연결된 모든 노드를 탐색한다.
            if not visited[i]:                              # 해당 노드를 방문한 적이 없다면
                next_node.append(i)                         # next_node에 추가한다.
                
        for _ in range(len(next_node)):                     # next_node의 원소 개수만큼 dfs를 수행해야한다.
            next = result.popleft()                         # dfs 탐색 결과에서 확인해야할 원소를 꺼낸다.
            if next in next_node:                           # 해당 원소가 next_node에 포함된다면(현재 노드와 연결되어 있다면)
                stack.append(next)                          # stack에 next를 추가하고 방문처리한다.
                visited[next] = True                        
                break
            else:                                           # 그렇지 않다면 0을 출력하고 함수를 종료한다.
                print(0)
                return

    print(1)                                                # dfs 탐색 결과가 올바르다는 의미이므로 1을 출력한다.

dfs()