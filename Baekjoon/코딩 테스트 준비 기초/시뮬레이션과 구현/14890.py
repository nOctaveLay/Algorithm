import sys
input = sys.stdin.readline

# init condition
n,l = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]




def check_road_return_boolean(arr,l):
    check_slove = [False for _ in range(len(arr))]
    for i in range(1,len(arr)):
        # 크기 차이가 1 이상인 경우 -> 경사로를 놓을 수 없다.
        if abs(arr[i]- arr[i-1]) > 1: return 0

        '''
        경사로를 놓아야 하는 경우는 data가 변화할 때밖에 없다.
        따라서 현재 data가 이전 data보다 큰 경우와
        현재 data가 이전 data보다 작은 경우로 나뉘어진다.
        '''

        # 현재 data가 이전 data보다 큰 경우 --> 이전 경로에 slove를 놓아야한다.
        if arr[i] > arr[i-1]:
            # 경사로 넓이만큼 체크
            for k in range(l):
                # 만약 경사로 넓이 안에 이미 사용된 경사로가 있거나, 범위를 벗어나거나, 아예 data가 다른 경우(연속해서 놓을 수 없음)
                # 범위를 먼저 확인해야 범위를 넘어갔을 때 check_slove, arr에서 문제가 안남
                if i-1-k < 0 or check_slove[i-1-k]  or arr[i-1-k] != arr[i-1]:
                    return 0
                else:
                    check_slove[i-1-k] = True

        # 현재 data가 이전 data보다 작은 경우 ---> 다음 경로에 slove를 놓아야한다.
        if arr[i] < arr[i-1]:
            # 경사로 넓이만큼 체크
            for k in range(l):
                # 경사로를 놓지 못하는 경우 -> 1. 이미 사용된 경사로가 있을 때, 2. arr의 범위를 벗어나서 놓을 수 없을 때 3. data가 연속적이지 않을 때
                # 범위를 먼저 확인해야 범위를 넘어갔을 때 check_slove, arr에서 문제가 안남

                if i+k > len(arr)-1 or check_slove[i+k] or arr[i] != arr[i+k]:
                    return 0
                else:
                    check_slove[i+k] = True
    return 1

# 가로 확인

count = 0
for row in arr:
    count += check_road_return_boolean(row,l)

# 세로 확인

for i in range(n):
    count += check_road_return_boolean([arr[j][i] for j in range(n)],l)

print(count)