import sys
input = sys.stdin.readline
n = int(input())
a,b = map(int,input().split())
max_profit = 0
satisfied_list = [[[[0]*4 for _ in range(110)] for _ in range(110)] for _ in range(110)]
arr_list = [list(map(int,input().split())) for _ in range(n)]

# bottom - up 방식으로 구현
def day_satisfy(days, rest_cnt, study_cnt, room):
    if days >= n:
        if rest_cnt <= a and study_cnt >= b: return 0
        return -999999
        
    if satisfied_list[days][rest_cnt][study_cnt][room] != 0: return satisfied_list[days][rest_cnt][study_cnt][room]

    satisfied_list[days][rest_cnt][study_cnt][room] = -999999
    # 공부를 했을 경우
    for i in range(2):
        satisfied_list[days][rest_cnt][study_cnt][room] = max(satisfied_list[days][rest_cnt][study_cnt][room],day_satisfy(days+1,rest_cnt,study_cnt+1,i) + arr_list[days][i])
    
    # 휴게실에서 공부를 했을 경우
    if room != 2:
        satisfied_list[days][rest_cnt][study_cnt][room] = max(satisfied_list[days][rest_cnt][study_cnt][room],day_satisfy(days+1,rest_cnt,study_cnt,2) + arr_list[days][2])

    # 휴게실에서 쉬었을 경우
    if rest_cnt < a:
        satisfied_list[days][rest_cnt][study_cnt][room] = max(satisfied_list[days][rest_cnt][study_cnt][room],day_satisfy(days+1,rest_cnt+1,study_cnt,3) + arr_list[days][3])
    return satisfied_list[days][rest_cnt][study_cnt][room]

ans = 0

case1 = day_satisfy(1, 0, 1, 0)+arr_list[0][0]
case2 = day_satisfy(1, 0, 1, 1)+arr_list[0][1]
case3 = day_satisfy(1, 0, 0, 2)+arr_list[0][2]
case4 = day_satisfy(1, 1, 0, 3)+arr_list[0][3]

print(max(case1,case2,case3,case4),end = '')
