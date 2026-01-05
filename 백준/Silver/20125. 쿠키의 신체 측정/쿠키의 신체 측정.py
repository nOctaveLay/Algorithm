import sys

input = sys.stdin.readline
n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]

# arr의 심장의 위치를 찾는 함수
def find_heart(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == '*':
                # 머리는 심장 바로 윗 칸에 한 칸 크기로 있으므로 
                # 처음 *를 찾은 곳(머리) 바로 아래 (i+1), j에 있다.
                # 문제에서 index가 1부터 시작하므로 (i+2), j+1에 위치
                return i+2, j+1

# 심장의 위치를 입력받고, 왼쪽 팔의 길이를 찾는 함수
# 주의, heart의 indexing은 1부터이다.
def find_left_length(arr,hr,hc):
    hr -= 1
    hc -= 1
    for c in range(hc):
        if arr[hr][c] == '*':
            return hc - c
    
def find_right_length(arr,hr,hc):
    hr -= 1
    hc -= 1
    for c in range(len(arr)-1,hc,-1):
        if arr[hr][c] == '*':
            return c-hc

def find_waist(arr,hr,hc):
    hr -= 1
    hc -= 1
    for r in range(len(arr)-1,hr,-1):
        if arr[r][hc] == '*':
            return r-hr
        
def find_left_leg(arr,hr,hc):
    hc -= 1
    for r in range(len(arr)-1,hr-1,-1):
        if arr[r][hc-1] == '*':
            return r-hr+1

def find_right_leg(arr,hr,hc):
    hc -= 1
    for r in range(len(arr)-1,hr-1,-1):
        if arr[r][hc+1] == '*':
            return r-hr+1


hr, hc = find_heart(arr)
print(hr, hc)
waist = find_waist(arr,hr,hc)
# print(find_right_leg(arr,hr+waist,hc))

print(find_left_length(arr,hr,hc), find_right_length(arr,hr,hc), waist, find_left_leg(arr,hr+waist,hc), find_right_leg(arr,hr+waist,hc))

