import sys

#외판원 순회 문제

def shortest_path(path,visited,cost):

    here = path[-1]

    # 기저 조건
    if len(path) == n and w[here][path[0]] != 0:
        return cost + w[here][path[0]]

    answer = sys.maxsize

    for next_visit in range(1,n):        
        if visited[next_visit] or (not w[here][next_visit]): continue
        else:
            visited[next_visit] = True
            path.append(next_visit)
            tsp = shortest_path(path,visited,cost+w[here][next_visit])
            answer = min(tsp,answer)
            path.pop()
            visited[next_visit] = False
    return answer


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    w = [list(map(int,input().split(" "))) for _ in range(n)]

    visited = [0] * n
    visited[0] = 1

    print(shortest_path([0],visited,0),end = '')