import sys

input= sys.stdin.readline

a,b = 0,0
for _ in range(2):
    i,j = map(int,input().split())
    a+=i
    b+=j
if a < b:
    print("Hanyang Univ.") 
elif a == b:
    print("Either")
else:
    print("Yongdap")