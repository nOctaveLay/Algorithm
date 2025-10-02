import sys

input = sys.stdin.readline
max_value = 0
snak_type = ['S', 'N', 'U']
max_idx = 0
for i in range(3):
    p, w = map(int,input().split())
    if p * 10 >= 5000 : p -= 50
    if max_value < (w/p):
        max_value = w/p
        max_idx = i

print(snak_type[max_idx])