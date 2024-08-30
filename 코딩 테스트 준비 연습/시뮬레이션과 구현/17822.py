from collections import deque
import sys
input = sys.stdin.readline

def rotate(x:int, d:int, k:int):
    # rotate circle
    rotate_num = 0
    if d == 0: rotate_num = k
    else: rotate_num = -k

    for circle_num in range(x-1,n,x):
        arr[circle_num].rotate(rotate_num)

    # remove_ circle
    # 인접하면서 같은 수들 찾기
    remove_set = set()
    for i in range(n):
        for j in range(m-1):
            if arr[i][j]:
                if arr[i][j] == arr[i][j+1]:
                    remove_set.add((i,j))
                    remove_set.add((i,j+1))
        if arr[i][0] and arr[i][0] == arr[i][-1]:
            remove_set.add((i,0))
            remove_set.add((i,m-1))

    for j in range(m):
        for i in range(n-1):
            if arr[i][j]:
                if arr[i][j] == arr[i+1][j]:
                    remove_set.add((i,j))
                    remove_set.add((i+1,j))

    find = len(remove_set)
    for position in remove_set:
        arr[position[0]][position[1]] = 0
    return find

def solution(x:int, d:int, k:int):
    all_num, all_sum = 0, 0
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                all_num += 1
                all_sum += arr[i][j]
    if all_num == 0: return
    avg = all_sum / all_num
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                if arr[i][j] > avg:
                    arr[i][j] -= 1
                elif arr[i][j] < avg:
                    arr[i][j] += 1

if __name__ == "__main__":
    n, m, t = map(int, input().split())
    arr = list(deque(map(int, input().split())) for _ in range(n))

    for _ in range(t):
        x, d, k = map(int, input().split())
        find = rotate(x,d,k)
        if not find: solution(x,d,k)

    result = 0
    for i in range(n):
        result += sum(arr[i])
    print(result)