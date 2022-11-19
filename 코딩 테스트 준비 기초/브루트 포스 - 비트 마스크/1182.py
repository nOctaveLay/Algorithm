import sys
input = sys.stdin.readline

n, s = map(int,input().split())
cnt = 0
arr = list(map(int,input().split()))
def count_cnt_and_sum_to_current_idx(idx,cur_sum):
    global cnt
    if idx > n-1 : return
    
    cur_sum += arr[idx]

    # s와 같다면 cnt 증가
    if cur_sum == s:
        cnt += 1

    # 내가 있는 이 위치를 선택했을 경우
    count_cnt_and_sum_to_current_idx(idx+1,cur_sum)

    # 내가 있는 위치를 선택하지 않았을 경우
    count_cnt_and_sum_to_current_idx(idx+1,cur_sum - arr[idx])

count_cnt_and_sum_to_current_idx(0,0)
print(cnt)