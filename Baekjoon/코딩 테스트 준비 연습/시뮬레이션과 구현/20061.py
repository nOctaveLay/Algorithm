import sys
input = sys.stdin.readline
blue_board = [[0 for _ in range(6)] for _ in range(4)]
green_board = [[0 for _ in range(4)] for _ in range(6)]
def remove_column(column:int):
    for j in reversed(range(column+1)):
        for i in range(4):
            blue_board[i][j] = blue_board[i][j-1]
    for i in range(4):
        blue_board[i][0] = 0

def remove_row(row:int):
    for i in reversed(range(row+1)):
        for j in range(4):
            green_board[i][j] = green_board[i-1][j]
    for j in range(4):
        green_board[0][j] = 0

# 점수 획득
def get_point_at_blue():
    point = 0
    for j in range(2,6):
        cnt = 0
        for i in range(4):
            cnt += blue_board[i][j]
        if cnt == 4:
            # 열 삭제
            remove_column(j)
            point += 1
    return point

def get_point_at_green():
    point = 0
    for i in range(2,6):
        cnt = 0
        for j in range(4):
            cnt += green_board[i][j]
        if cnt == 4:
            # 행 삭제
            remove_row(i)
            point += 1
    return point 

def move_blue(t,x):
    # blue board로 이동
    for column in range(1,6):
        if t == 3: # x,y 
            if column == 5 or blue_board[x][column+1] or blue_board[x+1][column+1]:
                blue_board[x][column] = 1
                blue_board[x+1][column] = 1
                break
        else:
            if column == 5 or blue_board[x][column+1]:
                blue_board[x][column] = 1
                if t == 2:
                    blue_board[x][column-1] = 1
                break

    # 열이 가득차면 blue_board 에서 해당 열 삭제 -> 점수 획득
    score = get_point_at_blue()

    for j in range(2):
        for i in range(4):
            if blue_board[i][j]:
                remove_column(5)
                break

    return score

def move_green(t,y):
    for row in range(1,6):
        if t == 2:
            if row == 5 or green_board[row+1][y] or green_board[row+1][y+1]:
                green_board[row][y] = 1
                green_board[row][y+1] = 1
                break
        else:
            if row == 5 or green_board[row+1][y]:
                green_board[row][y] = 1
                if t == 3:
                    green_board[row-1][y] = 1
                break


    score = get_point_at_green()

    for i in range(2):
        for j in range(4):
            if green_board[i][j]:
                remove_row(5)
                break
    return score
    
if __name__ == "__main__":

    blue_board = [[0 for _ in range(6)] for _ in range(4)]
    green_board = [[0 for _ in range(4)] for _ in range(6)]
    
    n = int(input())
    score = 0
    for _ in range(n):
        t,x,y = map(int, input().split())
        blue_score = move_blue(t,x)
        green_score = move_green(t,y)
        score += blue_score + green_score

    cnt = 0
    for i in range(4):
        for j in range(2, 6):
            if blue_board[i][j]:
                cnt += 1
    for i in range(2, 6):
        for j in range(4):
            if green_board[i][j]:
                cnt += 1

    print(score, cnt, sep='\n')