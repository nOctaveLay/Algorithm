import sys

input=sys.stdin.readline
h,w,n,m = map(int,input().split())

height_field = h//(n+1) if h%(n+1) == 0 else h//(n+1) +1
weight_field = w//(m+1) if w%(m+1) == 0 else w//(m+1) +1

print(height_field * weight_field)