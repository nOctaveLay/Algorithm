import sys
input=sys.stdin.readline
n,m,b=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

# 최솟값 / 최대값을 찾음
already_block = sum(sum(arr[i]) for i in range(n))
min_arr, max_arr = min(min(arr)), max(max(arr))
min_time, min_goal = 500*500*257*2+1, min_arr
for goal in range(min_arr, max_arr+1):
    # inventory 안의 블록으로 만들 수 있는지 먼저 체크
    if b >= (goal * m * n - already_block):
        time = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] < goal: # 블록을 채우는 작업
                    time += goal - arr[i][j] #1초씩 총 goal에 해당하는 만큼
                else: # 블록을 빼는 작업
                    time += (arr[i][j] - goal)*2
        # 답이 여러개 있을 경우 땅의 높이가 높은 걸로 결정.
        # min부터 차례로 max가 되므로, 땅의 높이가 더 높을 때 min_time이 같으면 자연스럽게 변경되도록
        if time <= min_time: 
            min_time = time
            min_goal = goal
print(min_time, min_goal)