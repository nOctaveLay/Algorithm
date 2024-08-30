import sys
ans = 0
n = int(sys.stdin.readline())
for i in range(1,n+1):
    ans += (n//i) *i
print(ans)