from itertools import combinations
import sys
input = sys.stdin.readline
n, l, r, x = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
for k in range(2, n + 1):
    for comb in combinations(arr, k):
        if l <= sum(comb) <= r:
            if max(comb) - min(comb) >= x:
                result += 1
print(result)