import re
import sys
input=sys.stdin.readline

t = int(input())
c = re.compile('(100+1+|01)+')
for _ in range(t):
    s = input().rstrip()
    a = c.fullmatch(s)
    if a == None:
        print("NO")
    else:
        print("YES")