import sys
input = sys.stdin.readline
n,m,x,y,k = map(int,input().split())

def return_moved_index(index_data,num):
    if num == 1: return [index_data[i-1] for i in (4,1,3,6,5,2)]
    elif num == 2 : return [index_data[i-1] for i in (2,6,3,1,5,4)]
    elif num == 3 : return [index_data[i-1] for i in (3,2,6,4,1,5)]
    else: return [index_data[i-1] for i in (5,2,1,4,6,3)]
  
dice_data = [0 for _ in range(6)]
index_ = [i for i in range(6)]
map_data = [list(map(int,input().split())) for _ in range(n)]

k_list = list(map(int,input().split()))
dx = [0,0,-1,1]
dy = [1,-1,0,0]

#cx : 세로, cy : 가로
cx,cy = x,y

for cmd in k_list:
    cx,cy = cx + dx[cmd-1], cy + dy[cmd-1]
    if cx >= 0 and cx < n and cy >= 0 and cy < m:
        index_ = return_moved_index(index_,cmd)
        if map_data[cx][cy] == 0:
            map_data[cx][cy] = dice_data[index_[0]]
        else:
            dice_data[index_[0]] = map_data[cx][cy]
            map_data[cx][cy] = 0
        print(dice_data[index_[-1]])

    else:
        cx,cy = cx - dx[cmd-1], cy - dy[cmd-1]
        

        


