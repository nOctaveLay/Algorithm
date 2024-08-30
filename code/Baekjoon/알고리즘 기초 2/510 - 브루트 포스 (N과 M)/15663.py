import sys
from itertools import permutations

input = sys.stdin.readline

n,m = map(int,input().split())
permutation_list = sorted(list(map(int,input().split())))
data_base = dict()

for i in permutations(permutation_list,m):
    if i not in data_base:
        print(*i,sep = ' ')
        data_base[i] = 1