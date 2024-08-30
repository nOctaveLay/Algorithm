from collections import deque
import sys

def bfs(input_answer):
    idx = 0
    result = 1
    visited = set()
    next_visit = deque()
    visited.add(input_answer[idx])
    next_visit.append(input_answer[idx])
    idx += 1
    while next_visit:
        nvp = next_visit.popleft()
        minus_group = set(graph[nvp]) - visited
        if set(input_answer[idx:idx + len(minus_group)]) == minus_group:
            for i in range(len(minus_group)):
                if not input_answer[idx+i] in visited:
                    next_visit.append(input_answer[idx+i])
                    visited.add(input_answer[idx+i])
            idx += len(minus_group)
        else: 
            result = 0
            break
    return result

def make_graph():
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    return graph

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    graph = make_graph()
    input_answer = list(map(int,input().split()))
    if input_answer[0] != 1: print(0)
    else: print(bfs(input_answer))