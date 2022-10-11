from bisect import bisect_left,bisect_right
import sys

# 이분 탐색
# 연속하면 반드시 accumulate부터 생각하자
def possible_sum(a:list):
    result = list()
    for i in range(len(a)):
        i_sum = 0
        for j in range(i,len(a)):
            i_sum += a[j]
            result.append(i_sum)
    return sorted(result)

if __name__ == "__main__":
    input = sys.stdin.readline
    t = int(input())
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))

    accumul_a = possible_sum(a)
    accumul_b = possible_sum(b)
    cnt = 0
    
    # 이진 탐색으로 갯수를 판단할 수 있다.
    for elem_a in accumul_a:
        l = bisect_left(accumul_b,t-elem_a)
        r = bisect_right(accumul_b,t-elem_a)
        cnt += abs(r-l)
    print(cnt)