# https://www.acmicpc.net/problem/17144
import sys
from copy import deepcopy
input = sys.stdin.readline

# 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
# (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
# 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
# 확산되는 양은 A(r,c)/5이고 소수점은 버린다.
# (r, c)에 남은 미세먼지의 양은 A(r,c) - (A(r,c)/5)×(확산된 방향의 개수) 이다.

def diffusion(a: list):
    d = [(1,0), (-1,0), (0,1), (0,-1)] # 인접한 4방향을 상대좌표로 표현
    result = [[0 for _ in range(c)] for _ in range(r)] # 확산이 전부 끝난 결과가 저장될 곳
    air_conditioner_pos = []
    for x in range(r):
        for y in range(c):
            if a[x][y] == -1: # 공기 청정기가 있는 곳은 움직이지 않는다.
                result[x][y] = -1
                air_conditioner_pos.append((x,y))
            elif a[x][y]: # 공기청정기가 있는 곳은 확산되지 않는다.
                count = 0 # 확산된 방향의 개수
                diffusion_amount = a[x][y] // 5
                
                # 확산되는 양 계산 -> 확산되는 곳에 위치.
                for dx, dy in d:
                    nx = x + dx
                    ny = y + dy
                    if not (0<=nx<r and 0<=ny<c): continue # 범위를 벗어난 곳은 확산되지 않는다.
                    if a[nx][ny] == -1: continue # 공기청정기가 있는 곳으로 확산되지 않는다.
                    count += 1
                    result[nx][ny] += diffusion_amount
                
                # 남아있는 양을 result[x][y]로 옮김
                result[x][y] += a[x][y] - diffusion_amount * count
    return air_conditioner_pos, result

def clockwise_dust(pos:tuple,a:list,temp:list):
    x, y = pos
    d = [(0,1),(1,0),(0,-1), (-1,0)]
    way = 0
    hx, hy = x, y
    
    while True:    
        nx, ny = hx + d[way][0], hy + d[way][1]
        if not (x<=nx<r and 0<=ny<c): 
            way = (way + 1) % 4
            nx, ny = hx + d[way][0], hy + d[way][1]
        if nx == x and ny == y: break
        if a[hx][hy] == -1:
            temp[nx][ny] = 0
        else:
            temp[nx][ny] = a[hx][hy]
        hx, hy = nx, ny
    return temp

def counterclockwise_dust(pos:tuple,a:list,temp:list):

    x, y = pos
    d = [(0,1), (-1,0),(0,-1), (1,0)]
    way = 0
    hx, hy = x, y
    
    while True:    
        nx, ny = hx + d[way][0], hy + d[way][1]
        if not (0<=nx<=x and 0<=ny<c): 
            way = (way + 1) % 4
            nx, ny = hx + d[way][0], hy + d[way][1]
        if nx == x and ny == y: break
        if a[hx][hy] == -1:
            temp[nx][ny] = 0
        else:
            temp[nx][ny] = a[hx][hy]
        hx, hy = nx, ny
    return temp

def operating_air_conditioner(air_conditioner_pos:list, a:list):
    temp = deepcopy(a)
    counterclockwise_dust(air_conditioner_pos[0],a,temp)
    clockwise_dust(air_conditioner_pos[1],a,temp)    
    return temp

def sum_dust(a:list):
    result = 0
    for i in range(r):
        for j in range(c):
            if a[i][j] != -1:
                result += a[i][j]
    return result

if __name__ == "__main__":
    # r : max_row, c: max_column, t: the execution time of air conditioner
    r, c, t = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(r)]
    for _ in range(t):
        air_conditioner_pos, a = diffusion(a)
        a = operating_air_conditioner(air_conditioner_pos, a)
    result = sum_dust(a)
    print(result)