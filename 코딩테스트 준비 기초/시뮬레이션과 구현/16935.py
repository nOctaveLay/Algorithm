import sys

input = sys.stdin.readline
n,m,r = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
cmd_list = list(map(int,input().split()))

# 출력 형식 -> not checked
def print_arr(arr):
    for arr_row_list in arr:
            print(*arr_row_list)

# 상하 반전 -> checked
def reverse_up_and_down(arr):
    return [arr[-i] for i in range(1,len(arr)+1)] 

# 좌우 반전 -> checked
def reverse_right_and_left(arr):
    return [[j for j in reversed(arr_row_list)] for arr_row_list in arr]

# 오른쪽으로 90도 회전 -> checked
def rotate_right_90degree(arr):
    result = [[0 for _ in range(len(arr))] for _ in range(len(arr[0]))]
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            result[i][j] = arr[len(arr)-1-j][i]
    return result

# 왼쪽으로 90도 회전 -> checked 
def rotate_left_90degree(arr):
    result = [[0 for _ in range(len(arr))] for _ in range(len(arr[0]))]
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            result[i][j] = arr[j][len(arr[0])-1-i]
    return result

# 1->2, 2->3, 3->4, 4->1
# subgroup right rotation  --- > checked
def rotate_right_subgroup(arr):
    num_of_row = len(arr)
    num_of_column = len(arr[0])
    result = [[0 for _ in range(num_of_column)] for _ in range(num_of_row)]

    half_of_row = num_of_row // 2
    half_of_column = num_of_column // 2

    # first section -> checked
    for i in range(half_of_row):
        for j in range(half_of_column):
            result[i][j] = arr[half_of_row+i][j]

    # second section -> checked
    for i in range(half_of_row):
        for j in range(half_of_column,num_of_column):
            result[i][j] = arr[i][j-half_of_column]

    # third section -> checked
    for i in range(half_of_row,num_of_row):
        for j in range(half_of_column):
            result[i][j] = arr[i][j + half_of_column]

    # forth section -> checked
    for i in range(half_of_row,num_of_row):
        for j in range(half_of_column,num_of_column):
            result[i][j] = arr[i - half_of_row][j]
    return result

#checked
def rotate_left_subgroup(arr):
    num_of_row = len(arr)
    num_of_column = len(arr[0])
    result = [[0 for _ in range(num_of_column)] for _ in range(num_of_row)]

    half_of_row = num_of_row // 2
    half_of_column = num_of_column // 2

    # first section --> checked
    for i in range(half_of_row):
        for j in range(half_of_column):
            result[i][j] = arr[i][j + half_of_column]

    # second section --> checked
    for i in range(half_of_row):
        for j in range(half_of_column,num_of_column):
            result[i][j] = arr[i + half_of_row][j]

    # third section 
    for i in range(half_of_row,num_of_row):
        for j in range(half_of_column):
            result[i][j] = arr[i - half_of_row][j]

    # forth section 
    for i in range(half_of_row,num_of_row):
        for j in range(half_of_column,num_of_column):
            result[i][j] = arr[i][j - half_of_column]
    return result

for cmd in cmd_list:
    if cmd == 1:
        arr = reverse_up_and_down(arr)
    elif cmd == 2:
        arr = reverse_right_and_left(arr)
    elif cmd == 3:
        arr = rotate_right_90degree(arr)
    elif cmd == 4:
        arr = rotate_left_90degree(arr)
    elif cmd == 5:
        arr = rotate_right_subgroup(arr)
    elif cmd == 6:
        arr = rotate_left_subgroup(arr)
    else:
        print("ERR")
print_arr(arr)