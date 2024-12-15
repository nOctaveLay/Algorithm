from bisect import bisect_left, bisect_right

n=int(input())
arr=sorted(list(map(int,input().split())))
m=int(input())
find_list=list(map(int,input().split()))
for k in find_list:
    i_left = bisect_left(arr,k)
    i_right = bisect_right(arr,k)
    print(i_right-i_left, end=' ')