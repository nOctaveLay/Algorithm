from collections import deque
import sys
#init
input = sys.stdin.readline
gears_list = []

# 문제 조건
t = int(input()) # the num of gears
for _ in range(t):
    gear_dq = deque(map(int,input().rstrip("\n")))
    gears_list.append(gear_dq)

k = int(input()) # the number of rotations

# 완전히 잘못 이해했음
# 회전하기 전에 다른 극이어야됌
# n ~ n+1의 연결관계를 확인한다.
def check_same_polarity(gears_list):
    return [gears_list[gear_idx][2] != gears_list[gear_idx+1][6] for gear_idx in range(0,len(gears_list)-1)]

def rotate_the_number_of_gear(gear_num, rotate_direction, gears_list):

    cur_gear = gear_num - 1

    # 회전 하기 전에 다른 극인지 확인
    check_same_polar = check_same_polarity(gears_list)
    # 회전
    gears_list[cur_gear].rotate(rotate_direction)
    # check_left
    left_rotate_direction = - rotate_direction
    for lidx in reversed(range(cur_gear)):
        if check_same_polar[lidx]:
            gears_list[lidx].rotate(left_rotate_direction)
            left_rotate_direction = -left_rotate_direction

        else: break
        
    # check_right
    right_rotate_direction = - rotate_direction
    for ridx in range(cur_gear,len(gears_list) - 1):
        if check_same_polar[ridx]:
            gears_list[ridx+1].rotate(right_rotate_direction)
            right_rotate_direction = -right_rotate_direction
        else: break
    return gears_list

for _ in range(k):
    gear_num, rotate_direction = map(int,input().split())
    gears_list = rotate_the_number_of_gear(gear_num,rotate_direction, gears_list)

count = 0
for gear in gears_list:
    if gear[0] == 1: count += 1
print(count)