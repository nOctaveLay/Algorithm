'''
이 파이썬 파일은 스파게티 코드라 pypy에서만 작동함. python으로 짜는 건 차후에
'''

import sys
input = sys.stdin.readline

def up_down_elem(arr,l):
    
    # i,j는 초기위치
    # m,k는 상대위치에서 움직일만한 거리
    result = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
    for i in range(0,len(arr),2**l):
        for j in range(0,len(arr),2**l):
            for m in range(2**l):
                for k in range(2**l):
                    result[i+m][j+k] = arr[i+2**l-m-1][j+k]
            
    return result


def left_right_elem(arr,l):
    
    # i,j는 초기위치
    # m,k는 상대위치에서 움직일만한 거리

    result = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
    for i in range(0,len(arr),2**l):
        for j in range(0,len(arr[0]),2**l):
            for m in range(2**l):
                for k in range(2**l):
                    result[i+m][j+k] = arr[i+m][j+2**l-k-1]
    return result


def rotate_90_right_elem(arr,l):
    result = [[0 for _ in range(len(arr))] for _ in range(len(arr[0]))]
    for i in range(0,len(arr[0]),2**l):
        for j in range(0,len(arr),2**l):
            for m in range(2**l):
                for k in range(2**l):
                    
                   result[i+m][j+k] = arr[i+2**l-k-1][j+m]
    return result

def rotate_90_left_elem(arr,l):
    result = [[0 for _ in range(len(arr))] for _ in range(len(arr[0]))]
    for i in range(0,len(arr[0]),2**l):
        for j in range(0,len(arr),2**l):
            for m in range(2**l):
                for k in range(2**l):
                    result[i+m][j+k] = arr[i+k][j+2**l-m-1]
    return result

'''
덩어리를 그대로 옮기는 경우 상대위치에서 이동한 만큼 그대로 복사해서 붙여넣어주면 되기 때문에
result와 arr에서의 m, k는 그대로 이동해주면 되고 (positive)
나머지 초기 위치만 변형해서 넣어주면된다.
'''

def up_down_all(arr,l):
    
    # i,j는 초기위치
    # m,k는 상대위치에서 움직일만한 거리
    result = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
    # 초기 위치 => i가 반전
    for i in range(0,len(arr),2**l):
        for j in range(0,len(arr),2**l):
            # 그대로 유지
            for m in range(2**l):
                for k in range(2**l):
                    result[i+m][j+k] = arr[-i+m-2**l][j+k]
    return result

def left_right_all(arr,l):
        
    # i,j는 초기위치
    # m,k는 상대위치에서 움직일만한 거리

    result = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
    for i in range(0,len(arr),2**l):
        for j in range(0,len(arr[0]),2**l):
            for m in range(2**l):
                for k in range(2**l):
                    result[i+m][j+k] = arr[i+m][-j-2**l+k]
    return result

def rotate_90_right_all(arr,l):
    result = [[0 for _ in range(len(arr))] for _ in range(len(arr[0]))]
    for i in range(0,len(arr[0]),2**l):
        for j in range(0,len(arr),2**l):
            for m in range(2**l):
                for k in range(2**l):
                    result[i+m][j+k] = arr[-j-2**l+m][i+k]
    return result


def rotate_90_left_all(arr,l):
    result = [[0 for _ in range(len(arr))] for _ in range(len(arr[0]))]
    for i in range(0,len(arr[0]),2**l):
        for j in range(0,len(arr),2**l):

            for m in range(2**l):
                for k in range(2**l):
                    result[i+m][j+k] = arr[j+m][-i+k-2**l]
    return result

def check_method(arr,k,l):
    if k == 1:
        return up_down_elem(arr,l)
    elif k == 2:
        return left_right_elem(arr,l)
    elif k == 3:
        return rotate_90_right_elem(arr,l)
    elif k == 4:
        return rotate_90_left_elem(arr,l)
    elif k == 5:
        return up_down_all(arr,l)
    elif k == 6:
        return left_right_all(arr,l)
    elif k == 7:
        return rotate_90_right_all(arr,l)
    else:
        return rotate_90_left_all(arr,l)

if __name__ == "__main__":
    n, r = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(2**n)]
    for _ in range(r):
        k,l = map(int,input().split())
        arr = check_method(arr,k,l)
    for i in arr:
        print(*i)