'''
이 문제는 단순히 개념을 생각하지 않고 풀어도 될 문제이지만,
implicit graph를 배웠으니까, 그걸 응용해보자
component 찾는 11724와 비슷한 문제이므로 dfs를 쓴다는 것을 알 수 있다.
따라서 dfs 갯수를 찾는 문제이다.
x좌표, y좌표 각각 dfs를 해줘서 각 방향별로 dfs가 뻗어나가게끔 해주면 된다.

'''
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input()) # 지도의 크기
map_matrix = [[int(i) for i in input().rstrip("\n")] for _ in range(n)]
mask = 2
num_of_house = list()

# 좌표에서 -1, +1 교차를 많이 이용하므로, dx, dy를 이용해서 표기해주는 게 훨씬 낫다.
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
    count = 0
    # 범위를 벗어났을 때엔 dfs 진행 불가.
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0
    
    if map_matrix[x][y] == 1:
        map_matrix[x][y] = 0
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            count += dfs(nx,ny)
        return count
        
    return 0

num_of_complex = 0
num_of_houses = list()
for i in range(n):
    for j in range(n):
        house = dfs(i,j)
        if house:
            num_of_complex += 1
            num_of_houses.append(house)
print(num_of_complex)
print(*sorted(num_of_houses),sep='\n',end = '')