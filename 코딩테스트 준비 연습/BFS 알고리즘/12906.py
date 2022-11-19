from collections import deque
import sys

def bfs(ina,inb,inc,incnt):
    visited = set()
    q = deque()
    q.append((ina,inb,inc,incnt))
    while q:
        a,b,c,cnt = q.popleft()
        state_abc = a + '.' + b + '.' + c
        if a == 'A' * len(a) and b == 'B' * len(b) and c == 'C' * len(c):
            print(cnt)
            exit(0)

        if not state_abc in visited:
            visited.add(state_abc)
            if len(a):
                q.append((a[:-1], b + a[-1], c, cnt+1))
                q.append((a[:-1], b, c + a[-1], cnt+1))
            if len(b):
                q.append((a + b[-1], b[:-1], c, cnt+1))
                q.append((a, b[:-1], c + b[-1], cnt+1))
            if len(c):
                q.append((a + c[-1], b, c[:-1], cnt+1))
                q.append((a, b + c[-1], c[:-1], cnt+1))

        


if __name__ == "__main__":
    input = sys.stdin.readline
    state = list(input()[2:].rstrip("\n") for _ in range(3))
    bfs(state[0],state[1],state[2],0)

