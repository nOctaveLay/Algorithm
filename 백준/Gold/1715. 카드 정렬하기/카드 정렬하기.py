import sys
import heapq

input = sys.stdin.readline

n = int(input())

arr = list(int(input()) for _ in range(n))
heapq.heapify(arr)

num_of_comparison = 0
while len(arr) != 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    num_of_comparison += (a+b)
    heapq.heappush(arr,a+b)
print(num_of_comparison)
