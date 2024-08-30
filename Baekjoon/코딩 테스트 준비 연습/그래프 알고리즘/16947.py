from collections import deque
import sys
sys.setrecursionlimit(10**6)

# 지하철 2호선 같은 노선도가 주어졌을 때라고 규정하고 있으므로
# 순환 노선만 체크하면 된다.
def dfs(start_position, current_position, cnt):
    global check, the_longest_circulation, visited
    if current_position == start_position and cnt >= 3: # 순환 노선이 있는 경우
        the_longest_circulation = [i for i in range(start_position, n+1) if (visited & (1<<i))]
        check = 1
        return
    if check : return 
    for i in graph[current_position]:
        if not (visited & (1<<i)):
            visited |= (1 << i)
            dfs(start_position,i,cnt+1)
            visited ^= (1 << i)
            
def distance():
    q = deque()
    result = [-1 for _ in range(n)]
    for i in the_longest_circulation:
        q.append(i)
        result[i-1] = 0
    while q:
        h = q.popleft()
        for i in graph[h]:
            if result[i-1] == -1:
                q.append(i)
                result[i-1] = result[h-1] + 1
    return result

if __name__ == "__main__":

    n = int(input())
    graph = [[] for _ in range(n+1)]
    the_longest_circulation = []
    for _ in range(n):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    check = 0
    visited = 0 # bitmask로 check
    for i in range(1,n+1):
        dfs(i,i,0)
        visited |= (1 << i)
        if check == 1:
            break
    print(*distance())