from collections import deque
import sys
input = sys.stdin.readline

n = int(input())  # 보드의 크기
board = [[0] * n for _ in range(n)]  # 0: 빈칸, 1: 뱀, 2: 사과

k = int(input())  # 사과의 개수
for _ in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = 2  # 사과 위치

l = int(input())  # 방향 변환 횟수
rotations = deque()
for _ in range(l):
    t, d = input().split()
    rotations.append((int(t), d))

# 방향: 오른쪽(0), 아래(1), 왼쪽(2), 위(3)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def rotate(direction, c):
    if c == 'L':
        return (direction - 1) % 4
    else:
        return (direction + 1) % 4

snake = deque()
snake.append((0, 0))  # 시작 위치
board[0][0] = 1  # 뱀의 몸 표시

time = 0
direction = 0

while True:
    time += 1
    head_r, head_c = snake[-1]
    nr, nc = head_r + dr[direction], head_c + dc[direction]

    # 벽에 부딪힘
    if not (0 <= nr < n and 0 <= nc < n):
        break

    # 자기 몸에 부딪힘
    if board[nr][nc] == 1:
        break

    # 이동
    if board[nr][nc] == 2:  # 사과가 있으면
        board[nr][nc] = 1
        snake.append((nr, nc))  # 몸만 늘림 (꼬리 안 줄임)
    else:
        board[nr][nc] = 1
        snake.append((nr, nc))
        tail_r, tail_c = snake.popleft()
        board[tail_r][tail_c] = 0  # 꼬리 제거

    # 회전할 시간인지 확인
    if rotations and rotations[0][0] == time:
        _, c = rotations.popleft()
        direction = rotate(direction, c)

print(time)
