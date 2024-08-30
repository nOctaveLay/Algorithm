from collections import deque
import sys
a,b,c = map(int,sys.stdin.readline().split())
tot = a + b + c

'''
1. 이 문제는 a,b,c를 대소비교 하는 것 같아 보이지만
"크기가 같지 않은 두 그룹"을 "고르"고 돌의 갯수가 "작은 쪽"은 x+x로 업데이트, 갯수가 "큰 쪽" 은 y-x개로 만든다.
즉 대소는 "뽑힌 두 그룹"만 비교하면 된다. => 시간이 없더라도 문제를 잘 읽자.

2. a, b, c를 모두 visited로 만들려면 500 * 500 * 500 최소 125 * 10 ** 6 이라는 크기가 필요하다. 이는 반드시 512MB를 넘으므로 부적절하다.
따라서 최소/최대만 visited로 만들어 줄 필요가 생겼다.

3. 모든 visited를 확인할 필요가 없다는 점을 이용하여, visited를 set을 이용해서 만들어주었다.

'''

def bfs(a,b,c):

    # 방문해야 할 노드 저장
    # 각 노드는 (min값, max값) 으로 표현된다.
    q = deque()
    visited = set()

    min_init = min(a,b,c)
    max_init = max(a,b,c)

    q.append((min_init,max_init)) 
    visited.add((min_init,max_init))

    while q:
        ha,hb = q.popleft()
        hc = tot - (ha + hb)

        # 종료 조건은 현재 있는 노드의 값이 모두 같을 경우 종료된다.
        if ha == hb == hc: return 1

        for na, nb in ((ha, hb), (ha, hc), (hb, hc)):
            
            # +를 먼저 한 다음 -를 하면 2배로 빠지니 주의.'
            # 항상 순서를 기억할 것.
            
            if na < nb:
                nb -= na
                na += na

            elif na > nb:
                na -= nb
                nb += nb

            nc = tot - (na + nb)

            nmin = min(na, nb, nc)
            nmax = max(na, nb, nc)

            if (nmin, nmax) not in visited:
                q.append((nmin,nmax))
                visited.add((nmin, nmax))
    return 0

if tot % 3 != 0: print(0,end = '')
else: print(bfs(a,b,c),end = '')