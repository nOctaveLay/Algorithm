import sys
input = sys.stdin.readline
from collections import deque

#입력
cogwheels = list(deque(map(int,input().rstrip())) for _ in range(4))


def rotate_cog(cog_idx, direction):
    # 회전 방향 정보 저장
    rotations = [0] * 4
    rotations[cog_idx] = direction

    # 왼쪽 톱니바퀴 회전
    for i in range(cog_idx, 0, -1):
        if cogwheels[i][6] != cogwheels[i-1][2]:
            rotations[i-1] = -rotations[i]
        else:
            break

    # 오른쪽 톱니바퀴 회전
    for i in range(cog_idx, 3):
        if cogwheels[i][2] != cogwheels[i+1][6]:
            rotations[i+1] = -rotations[i]
        else:
            break
    
    for i in range(4):
        if rotations[i] != 0:
            cogwheels[i].rotate(rotations[i])


n = int(input())
for _ in range(n):
    cog_idx, direction = map(int,input().split())
    rotate_cog(cog_idx-1, direction)

answer = sum(cogwheels[i][0] * (2 ** i) for i in range(4))
print(answer)