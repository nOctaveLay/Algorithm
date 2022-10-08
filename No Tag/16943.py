from re import I
import sys
a,b = map(int,input().split())

k = set()
for i in str(a):
    k.add(int(i))
for j in str(b):
    k.add(int(j))
