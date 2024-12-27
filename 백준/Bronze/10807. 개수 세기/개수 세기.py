import sys
from collections import Counter
input=sys.stdin.readline
n=int(input())
arr=Counter(map(int, input().rstrip().split()))
print(arr[int(input())])