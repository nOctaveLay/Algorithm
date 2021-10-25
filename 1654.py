import random

k,n = map(int,input().split(" "))
len_lan_line = [int(input()) for _ in range(k)]

# Lamda : 
# input : 주어진 랜선의 길이, 잘라야 하는 랜선의 길이
# Output : 갯수가 출력
def sum_lan_line (cut_lan_line : int): return sum(l // cut_lan_line for l in len_lan_line)

end = max(len_lan_line) + 1
start = 1
# sum_lan_line(i) >= N 이 True 이고, sum_lan_line(i+1) >= N이 False인 i를 찾아야 한다.
# 이 i는 binary search로 찾을 수 있다. i는 max(len_lan_line)을 넘지 않는 정수이고, 최소 값은 1이다.


while True:
    mid = (start+end)//2

    # mid = end인 경우에 잘못될 수도 있음
    if sum_lan_line(mid) >= n and sum_lan_line(mid+1) < n: 
        print(mid)
        break
    elif sum_lan_line(mid) >= n:
        start = mid
    else: end = mid
