import sys

def return_min_length_of_seq():
    s,e = 0,1
    min_length = 100001
    while s < n:
        prefix_sum = sum_arr[e] - sum_arr[s]
        if prefix_sum >= m:
            if e-s < min_length:
                min_length = e-s
            s += 1
        elif e == n:
            s += 1
        else:
            e += 1
    return min_length if min_length != 100001 else 0

if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int,input().split())
    arr = list(map(int,input().split()))
    sum_arr = [0 for _ in range(n+1)]
    for i, arr_elem in enumerate(arr,start = 1):
        sum_arr[i] = sum_arr[i-1] + arr_elem
    print(return_min_length_of_seq())