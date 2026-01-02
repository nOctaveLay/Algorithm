import sys

input = sys.stdin.readline

# 초기 설정
'''
www
www
www [0]
rrr     bbb      ooo      ggg
rrr     bbb      ooo      ggg
rrr [1] bbb [2]  ooo [3]  ggg [4]
yyy
yyy
yyy [5]

'''

cube = [[['w','w','w'] for _ in range(3)],
    [['r','r','r'] for _ in range(3)],
    [['b','b','b'] for _ in range(3)],
    [['o','o','o'] for _ in range(3)],
    [['g','g','g'] for _ in range(3)],
    [['y','y','y'] for _ in range(3)]]

# 움직임 구현
# 한 면을 회전 시키면 정면에서 봤을 때 그 면은 회전된 상태가 됨
def move_itself(i): #i: 면의 위치
    temp = cube[i][0][0]
    cube[i][0][0] = cube[i][2][0]
    cube[i][2][0] = cube[i][2][2]
    cube[i][2][2] = cube[i][0][2]
    cube[i][0][2] = temp
    temp = cube[i][0][1]
    cube[i][0][1] = cube[i][1][0]
    cube[i][1][0] = cube[i][2][1]
    cube[i][2][1] = cube[i][1][2]
    cube[i][1][2] = temp

# 움직임을 받고 그에 맞춰서 회전
def move_cube(direction,side):
    if side == '+':
        if direction == 'U':
            move_itself(0) # 흰색 면 회전
            temp = cube[1][0]
            cube[1][0] = cube[2][0]
            cube[2][0] = cube[3][0]
            cube[3][0] = cube[4][0]
            cube[4][0] = temp

        elif direction == 'D':
            move_itself(5) # 노란면 회전
            temp = cube[1][2]
            cube[1][2] = cube[4][2]
            cube[4][2] = cube[3][2]
            cube[3][2] = cube[2][2]
            cube[2][2] = temp

        elif direction == 'F':
            move_itself(1) # 빨간면 회전
            temp = cube[0][2]
            # 일일히 대입하면 temp는 참조값을 가져오기 때문에.. temp값이 변질됨
            # 이 방식대로 하면 변조될 일은 없다. 근데 왜 그런지 모르겠음..
            cube[0][2] = [cube[4][2][2], cube[4][1][2], cube[4][0][2]] # g-> w
            cube[4][0][2], cube[4][1][2], cube[4][2][2]  = cube[5][0][0],cube[5][0][1],cube[5][0][2] # y -> g
            cube[5][0][0], cube[5][0][1], cube[5][0][2] = cube[2][2][0], cube[2][1][0], cube[2][0][0]
            cube[2][0][0], cube[2][1][0], cube[2][2][0] = temp[0], temp[1], temp[2] # w -> b

        elif direction == 'B':
            move_itself(3)
            temp = cube[0][0]
            cube[0][0] = [cube[2][0][2],cube[2][1][2],cube[2][2][2]]
            cube[2][0][2], cube[2][1][2], cube[2][2][2] = [cube[5][2][2], cube[5][2][1], cube[5][2][0]]
            cube[5][2][0], cube[5][2][1], cube[5][2][2] = [cube[4][0][0], cube[4][1][0], cube[4][2][0]]
            cube[4][0][0], cube[4][1][0], cube[4][2][0] = [temp[2], temp[1], temp[0]]
 
        elif direction == 'L':
            move_itself(4)
            temp = [cube[0][0][0], cube[0][1][0], cube[0][2][0]]
            cube[0][0][0], cube[0][1][0], cube[0][2][0] = [cube[3][2][2], cube[3][1][2], cube[3][0][2]]
            cube[3][2][2], cube[3][1][2], cube[3][0][2] = [cube[5][0][0], cube[5][1][0], cube[5][2][0]]
            cube[5][0][0], cube[5][1][0], cube[5][2][0] = [cube[1][0][0], cube[1][1][0], cube[1][2][0]]
            cube[1][0][0], cube[1][1][0], cube[1][2][0] = [temp[0], temp[1], temp[2]]

        elif direction == 'R':
            move_itself(2)
            temp = [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
            cube[0][0][2], cube[0][1][2], cube[0][2][2] = [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
            cube[1][0][2], cube[1][1][2], cube[1][2][2] = [cube[5][0][2], cube[5][1][2], cube[5][2][2]]
            cube[5][0][2], cube[5][1][2], cube[5][2][2] = [cube[3][2][0], cube[3][1][0], cube[3][0][0]]
            cube[3][0][0], cube[3][1][0], cube[3][2][0] = [temp[2], temp[1], temp[0]]
    else:
        move_cube(direction,'+')
        move_cube(direction,'+')
        move_cube(direction,'+')

def print_front():
    for i in range(3):
        print(*cube[0][i],sep='')

#U: 윗 면, D: 아랫 면, F: 앞 면, B: 뒷 면, L: 왼쪽 면, R: 오른쪽 면

# move_cube('D','-')
# # print(cube)
# move_cube('R','+')
# print(cube)
# move_cube('F','-')
# print(cube)
# move_cube('F','-')
# print(cube)
# move_cube('L','+')
# # print(cube)
# move_cube('D','+')
# move_cube('F','+')
# move_cube('R','+')
# print(cube)
# print(cube)
n = int(input())
for i in range(n):
    cube = [[['w','w','w'] for _ in range(3)],
        [['r','r','r'] for _ in range(3)],
        [['b','b','b'] for _ in range(3)],
        [['o','o','o'] for _ in range(3)],
        [['g','g','g'] for _ in range(3)],
        [['y','y','y'] for _ in range(3)]]
    k = int(input())
    opers = list(input().rstrip().split())
    for r in range(k):
        move_cube(opers[r][0],opers[r][1])
    print_front()