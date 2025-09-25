import sys
input = sys.stdin.readline
from collections import deque

#입력
cogwheels = list(deque(map(int,input().rstrip())) for _ in range(4))

def check_left(c_i,r_d):
    # A 톱니바퀴 6번과 B 톱니바퀴 2번 확인
    if c_i - 1 < 0 : return

    if cogwheels[c_i][6] != cogwheels[c_i-1][2]:
        check_left(c_i-1,-r_d)
        cogwheels[c_i-1].rotate(-r_d)

def check_right(c_i,r_d):
    # A 톱니바퀴 2번과 B 톱니바퀴 6번 확인
    if c_i + 1 > 3 : return

    if cogwheels[c_i][2] != cogwheels[c_i+1][6]:
        check_right(c_i+1,-r_d)
        cogwheels[c_i+1].rotate(-r_d)

n = int(input())
for _ in range(n):
    c_i, r_d = map(int,input().split())
    c_i -= 1
    check_left(c_i,r_d)
    check_right(c_i,r_d)
    cogwheels[c_i].rotate(r_d)

answer = 0
for index, cogwheel in enumerate(cogwheels):
    answer += cogwheel[0] * (2**index)
print(answer)