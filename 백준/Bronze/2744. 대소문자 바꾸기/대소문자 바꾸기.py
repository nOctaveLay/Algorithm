import sys
input=sys.stdin.readline
str=input().rstrip()
result=''
for c in str:
    if c.isupper():
        result += c.lower()
    if c.islower():
        result += c.upper()
print(result)