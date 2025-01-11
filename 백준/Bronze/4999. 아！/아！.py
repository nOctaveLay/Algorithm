import sys
input=sys.stdin.readline
a,b = input().rstrip(), input().rstrip()
answer = 'go' if len(a) >= len(b) else 'no'
print(answer)