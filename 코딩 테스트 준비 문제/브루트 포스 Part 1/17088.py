from copy import deepcopy
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
min_value = 10 ** 9 + 1
def check(temp_arr:list,d:int,count:int):
    for i in range(2,n):
        check_d = temp_arr[i]- temp_arr[i-1]
        if abs(check_d - d) > 1 : return -1
        else:
            if check_d != d:
                count += 1
                temp_arr[i] = temp_arr[i-1] + d
    return count
if len(arr) == 1:
    min_value = 0
else:
    # 0번째, 1번째 결정
    for zero_oper in [-1,0,1]:
        a1 = arr[0] + zero_oper
        for one_oper in [-1,0,1]:
            a2 = arr[1] + one_oper
            count = 0 
            if zero_oper: count += 1
            if one_oper: count += 1
            temp_arr = deepcopy(arr)
            temp_arr[0] = a1
            temp_arr[1] = a2
            # 나머지 check
            count = check(temp_arr,a2-a1,count)
            if count == -1: continue
            else: min_value = min(min_value,count)

print(min_value if min_value != 10 ** 9 + 1 else -1)