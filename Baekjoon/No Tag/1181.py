import sys
input = sys.stdin.readline
iter_num = int(input())

names = [input().rsplit('\n') for _ in range(iter_num)]
names = sorted(names)
print(names)
