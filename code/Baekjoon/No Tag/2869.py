import sys
a,b,v = map(int,sys.stdin.readline().split())

if (v-a) % (a-b) == 0:
    k = (v-a) // (a-b)
else:
    k = (v-a) // (a-b) + 1
print(k + 1)