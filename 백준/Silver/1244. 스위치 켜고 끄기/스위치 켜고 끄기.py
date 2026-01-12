import sys

input = sys.stdin.readline

s_n = int(input())
arr = list(map(int, input().split()))
p_n = int(input())

for _ in range(p_n):
    g, g_n = map(int, input().split())
    # 남성일 경우
    if g == 1:
        # 스위치의 배수에 해당하는 걸 바꾼다.
        # 단 arr의 index 는 0부터, 스위치는 1부터 시작한다.
        for i in range(g_n-1,s_n,g_n):
            arr[i] = (arr[i] + 1) % 2
    # 여성일 경우
    else:
        # 대칭 확인
        # 기준점 : g_n -1
        arr[g_n-1] = (arr[g_n-1] + 1) % 2
        for i in range(1,g_n):
            if g_n-1+i > s_n-1: break
            if arr[g_n-1-i] == arr[g_n-1+i]:
                arr[g_n-1-i] = (arr[g_n-1-i]+1) % 2
                arr[g_n-1+i] = (arr[g_n-1+i]+1) % 2
            else:
                break

end = len(arr)//20 + 1 if len(arr) % 20 != 0 else len(arr)//20
for i in range(end):
    print(*arr[i*20:(i+1)*20])