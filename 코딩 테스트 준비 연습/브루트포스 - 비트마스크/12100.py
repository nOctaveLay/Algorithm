from copy import deepcopy
import sys
input = sys.stdin.readline

def return_max_value_in_array(arr):
    global max_value
    for i in arr:
        max_value = max(max_value,max(i))

def move_up(arr):
    for j in range(len(arr[0])):
        num_position = 0
        for i in range(1,len(arr)):
            if arr[i][j] == 0: continue
            temp_arr = arr[i][j]
            arr[i][j] = 0

            if arr[num_position][j] == 0:
                arr[num_position][j] = temp_arr  

            elif arr[num_position][j] == temp_arr:
                arr[num_position][j] <<= 1
                num_position += 1
            else:
                num_position += 1
                arr[num_position][j] = temp_arr
    return arr

def move_down(arr):
    for j in range(len(arr[0])):
        num_position = len(arr)-1
        for i in reversed(range(len(arr)-1)):
            if arr[i][j] == 0: continue
            temp_arr = arr[i][j]
            arr[i][j] = 0

            if arr[num_position][j] == 0:
                arr[num_position][j] = temp_arr  

            elif arr[num_position][j] == temp_arr:
                arr[num_position][j] <<= 1
                num_position -= 1
            else:
                num_position -= 1
                arr[num_position][j] = temp_arr
    return arr

def move_left(arr):
    for i in range(len(arr)):
        num_position = 0

        for j in range(1,len(arr[0])):
            if arr[i][j] == 0: continue

            temp_arr = arr[i][j]
            arr[i][j] = 0 #이미 할당했다고 생각하고 0으로 만든다.

            if arr[i][num_position] == 0:
                arr[i][num_position] = temp_arr  

            elif arr[i][num_position] == temp_arr:
                arr[i][num_position] <<= 1
                num_position += 1
            else:
                num_position += 1
                arr[i][num_position] = temp_arr
                
    return arr

# num_position과 j가 같은 경우
# 뒤에 arr[i][j] = 0이라 선언하면
# 할당을 해주고 나서 그 수를 삭제해버린다. => 즉 이동은 안되고 0으로 수정
# 따라서 미리 0으로 만들고, 할당을 나중에 한다.
def move_right(arr):
    for i in range(len(arr)):
        num_position = len(arr) - 1

        for j in reversed(range(len(arr[0])-1)):
            if arr[i][j] == 0: continue
            temp_arr = arr[i][j]
            arr[i][j] = 0 #이미 할당했다고 생각하고 0으로 만든다.

            if arr[i][num_position] == 0:
                arr[i][num_position] = temp_arr  

            elif arr[i][num_position] == temp_arr:
                arr[i][num_position] <<= 1
                num_position -= 1
            else:
                num_position -= 1
                arr[i][num_position] = temp_arr
                
    return arr

def move_board(arr,d):
    
    # 위 이동
    if d == 1:
        move_up(arr)
    # 아래 이동
    elif d == 2:
        move_down(arr)
    # 왼쪽 이동
    elif d == 3:
        move_left(arr)
    # 오른쪽 이동
    elif d == 4:
        move_right(arr)
    return arr


def dfs(board,cnt):
    if cnt == 5:
        return_max_value_in_array(board)
        return 
    for i in range(1,5):
        # dfs가 끝난 후엔 원 상태의 board로 돌아와야 하기 때문에 copy값을 넘겨준다.
        next_board = move_board(deepcopy(board),i)
        dfs(next_board,cnt + 1)

if __name__ == "__main__":

    n = int(input())

    arr = [list(map(int,input().split())) for _ in range(n)]
    max_value = 0
    dfs(arr,0)
    print(max_value)