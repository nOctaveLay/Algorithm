import sys
input = sys.stdin.readline

def return_moved_index(num):
    if num == 0: return [index_[i-1] for i in (4,1,3,6,5,2)]
    elif num == 1 : return [index_[i-1] for i in (2,6,3,1,5,4)]
    elif num == 2 : return [index_[i-1] for i in (3,2,6,4,1,5)]
    else: return [index_[i-1] for i in (5,2,1,4,6,3)]

def return_cmd(cmd):
    if cmd == 0 : ncmd = 1
    elif cmd == 1 : ncmd = 0
    elif cmd == 2 : ncmd = 3
    elif cmd == 3: ncmd = 2
    return ncmd

def dfs(start):
    global index_
    for cmd in range(4):
        cx,cy = start[0] + dx[cmd], start[1] + dy[cmd]
        if cx >= 6*k and cx < 6*(k+1) and cy >= 0 and cy < 6 and visited[cx][cy] == 0:
            if map_data[cx][cy] == 1:
                index_ = return_moved_index(cmd)
                dice_data[index_[0]] = map_data[cx][cy]
                visited[cx][cy] = 1
                dfs([cx,cy])
                ncmd = return_cmd(cmd)
                index_ = return_moved_index(ncmd)

def check_dice_data(dice_data):
    for dd in dice_data:
        if dd == 0:
            return "no"
    return "yes"

if __name__ == "__main__":
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    map_data = [list(map(int,input().split())) for _ in range(18)]
    visited = [[0 for _ in range(6)] for _ in range(18)]
    start = []
    for k in range(3):
        dice_data = [0 for _ in range(6)]
        index_ = [i for i in range(6)]
        for i in range(k*6, (k+1)*6):
            for j in range(6):
                if visited[i][j] == 0 and map_data[i][j] == 1:
                    dice_data[0] = 1
                    dfs([i,j])
        print(check_dice_data(dice_data))

