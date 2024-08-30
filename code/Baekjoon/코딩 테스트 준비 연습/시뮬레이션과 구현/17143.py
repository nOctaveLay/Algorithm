# https://www.acmicpc.net/problem/17143
import sys
input = sys.stdin.readline


'''
첫째 줄에 격자판의 크기 R, C와 상어의 수 M이 주어진다. 
둘째 줄부터 M개의 줄에 상어의 정보가 주어진다. 
상어의 정보는 다섯 정수 r, c, s, d, z (1 ≤ r ≤ R, 1 ≤ c ≤ C, 0 ≤ s ≤ 1000, 1 ≤ d ≤ 4, 1 ≤ z ≤ 10000) 로 이루어져 있다. 
(r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다. 
d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
두 상어가 같은 크기를 갖는 경우는 없고, 하나의 칸에 둘 이상의 상어가 있는 경우는 없다.

출력
낚시왕이 잡은 상어 크기의 합을 출력한다.'''

def move_shark(shark_infos:list):
    d = [(-1,0), (1,0), (0,1), (0,-1)] # d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
    new_shark_infos = [[[] for _ in range(c)] for _ in range(r)] # 3 * 100 * 100 = 충분히 가능.
    for i in range(r):
        for j in range(c):
            if len(shark_infos[i][j]) != 0:
                shark_v, shark_d, shark_s = shark_infos[i][j]

                # 실제 옮겨야 하는 move를 알려면, 움직여서 처음으로 돌아가는 move를 빼야한다.
                if shark_d == 0 or shark_d == 1:
                    shark_v %= 2 * (r-1)
                else:
                    shark_v %= 2 * (c-1)
                
                # 이동시키기
                hx, hy = i,j
                for _ in range(shark_v):
                    dx, dy = d[shark_d]
                    nx, ny = hx + dx, hy + dy

                    # 만약 가야할 곳이 범위를 넘어간다 -> 가는 방향을 바꿔줌
                    if not (0<=nx<r and 0<=ny<c):
                        dx, dy = -dx, -dy
                        shark_d = shark_d + 1 if shark_d % 2 == 0 else shark_d - 1
                        nx, ny = hx + dx, hy + dy
                    hx, hy = nx, ny

                # 상어의 정보 쓰기
                if len(new_shark_infos[hx][hy]) != 0:
                    _, _, current_shark_s = new_shark_infos[hx][hy]
                    if current_shark_s < shark_s:
                        new_shark_infos[hx][hy] = [shark_v, shark_d, shark_s]
                else:
                    new_shark_infos[hx][hy] = [shark_v, shark_d, shark_s]
                    
    return new_shark_infos


def solution(shark_infos:list):
    catch_shark_scales = []
    for person_c in range(c):
        for shark_r in range(r):
            if shark_infos[shark_r][person_c]:
                # 땅과 가장 가까운 상어를 잡는다. = row가 적으면 적을 수록 땅과 가까운 상어이다.
                catch_shark_scales.append(shark_infos[shark_r][person_c][-1])
                # 잡힌 상어는 더 이상 바닷속에 존재하지 않는다.
                shark_infos[shark_r][person_c] = []
                break
        # 상어가 이동한다.
        shark_infos = move_shark(shark_infos)
    return sum(catch_shark_scales)
        

# 낚시왕이 오른쪽으로 한 칸 이동한다.
# 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
# 상어가 이동한다.
# 낚시왕은 가장 오른쪽 열의 오른쪽 칸에 이동하면 이동을 멈춘다.

if __name__ == "__main__":
    r, c, m = map(int,input().split()) # 격자판의 크기 r,c 상어의 수 m
    shark_infos = [[[] for _ in range(c)] for _ in range(r)] # 3 * 100 * 100 = 충분히 가능.
    
    # 상어 정보 분석
    for _ in range(m):
        # (r,c) : 위치, v: 속력, d: 이동방향, s: 크기
        shark_r, shark_c, shark_v, shark_d, shark_s = map(int,input().split())
        shark_infos[shark_r-1][shark_c-1] = [shark_v, shark_d-1, shark_s]
    print(solution(shark_infos), end='')