import sys
input = sys.stdin.readline
from copy import deepcopy

cube_data = [0] + list(map(int, input().split()))

def ccw_rotate_x(cube:list):
    init_a, init_b = cube[22], cube[24]
    cube[22], cube[24] = cube[9], cube[11]
    cube[9], cube[11] = cube[5], cube[7]
    cube[5], cube[7] = cube[1], cube[3]
    cube[1], cube[3] = init_a, init_b
    return cube

def ccw_rotate_y(cube:list):
    init_a, init_b = cube[17], cube[19]
    cube[17], cube[19] = cube[10], cube[9]
    cube[10], cube[9] = cube[16], cube[14]
    cube[16], cube[14] = cube[3], cube[4]
    cube[3], cube[4] = init_a, init_b
    return cube

def ccw_rotate_z(cube:list):
    init_a, init_b = cube[21], cube[22]
    cube[21], cube[22] = cube[17], cube[18]
    cube[17], cube[18] = cube[5], cube[6]
    cube[5], cube[6] = cube[13], cube[14]
    cube[13], cube[14] = init_a, init_b
    return cube

def cw_rotate_x(cube:list):
    for _ in range(3):
        cube = ccw_rotate_x(cube)
    return cube

def cw_rotate_y(cube:list):
    for _ in range(3):
        cube = ccw_rotate_y(cube)
    return cube

def cw_rotate_z(cube:list):
    for _ in range(3):
        cube = ccw_rotate_z(cube)
    return cube

def check_all_surface(cube:list):
    for i in range(6):
        for j in range(1, 4):
            if cube[4 * i + j] != cube[4 * i + (j + 1)]:
                return False
    return True

for func in [cw_rotate_x, cw_rotate_y, cw_rotate_z, ccw_rotate_x, ccw_rotate_y, ccw_rotate_z]:
    cube = cube_data[:]
    cube = func(cube)
    if check_all_surface(cube):
        print(1)
        exit()
print(0)