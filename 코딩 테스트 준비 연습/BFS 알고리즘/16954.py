# That's why 자료구조가 중요한 이유
from collections import deque
from itertools import product
import sys
def bfs():
    d = set(product([-1,0,1],repeat= 2))
    start = (7,0)
    q = deque()
    q.append((start[0],start[1]))
    lev = 0
    while lev < 8:
        lev += 1
        for _ in range(len(q)):
            sr, sc = q.popleft()
            if sr == 0 and sc == 7: # 오른쪽 위로 갔다면
                return 1 # 도착했다고 알려라
            for dx,dy in d:
                nr, nc = sr + dx, sc + dy
                # nr,nc가 범위 안에 있고, 다음에 지나갈 장소가 벽으로 막혀있지 않다면
                if (0<=nr<8 and 0<=nc<8) and not arr[nr][nc]:
                    if nr >= 1 and arr[nr-1][nc] == 1: continue
                    q.append((nr,nc))
        q = deque(set(q))
        # board의 밑을 지우고, 위를 빈칸으로 넣으면 된다.
        # 앞에서부터 내려버리면 덮어쓰기 당하니 주의.
        arr.pop() # 마지막을 지운다.
        arr.appendleft([0 for _ in range(8)]) # 처음에 0으로 가득찬 board를 넣는다.

    if q: return 1
    else: return 0

if __name__ == "__main__":
    input = sys.stdin.readline
    arr = [list(input().rstrip("\n")) for _ in range(8)]
    arr = deque(list(map(lambda x : 0 if x =='.' else 1,b)) for b in arr)
    print(bfs())