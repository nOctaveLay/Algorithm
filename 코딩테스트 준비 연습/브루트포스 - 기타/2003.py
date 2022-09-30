import sys
# 연속합이 M이 된다는 것에 주의할 것.
# 연속합이므로, Two pointer algorithm이 유용하다.

def return_num_of_cases_of_sum():
    s,e = 0,0
    cnt = 0
    while s < n:
        prefix_sum = sum(arr[s:e])
        if prefix_sum == m:
            cnt += 1
            s += 1
        elif prefix_sum > m:
            s += 1
        elif e == n:
            s += 1
        else: e += 1
    return cnt


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int,input().split())
    arr = list(map(int,input().split()))
    print(return_num_of_cases_of_sum())