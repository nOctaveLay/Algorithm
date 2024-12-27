import sys
input=sys.stdin.readline
t=int(input())

sys.setrecursionlimit(3000)
for _ in range(t):
    m,n,k=map(int,input().split())
    
    # arr 초기화
    arr=[[0] * m for _ in range(n)]
    for _ in range(k):
        one_x, one_y = map(int,input().split())
        arr[one_y][one_x] = 1
    
    # dfs 구현
    def dfs(x,y):
        if arr[y][x]: # 배추가 있는 부분에만 지렁이를 놔야 한다.
            arr[y][x] = 0
            for next_x, next_y in [(x-1,y), (x+1, y), (x,y+1), (x, y-1)]:
                if next_x < 0 or next_x > m-1: continue
                if next_y < 0 or next_y > n-1: continue
                if arr[next_y][next_x]: # 다음에 갈 곳도 1이라면 방문해서 0으로 만들어주기
                    dfs(next_x, next_y)
    cnt = 0
    for y in range(n):
        for x in range(m):
            if arr[y][x] : 
                dfs(x,y)
                cnt += 1
    print(cnt)