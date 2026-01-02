import sys

input = sys.stdin.readline

# 최대 100*4 = 400번
n = int(input())
arr = list(input().rstrip() for _ in range(n))
answer = ''
index1, index2 = 0, 0

for i in range(n):
    if arr[i] == 'KBS1':
        index1 = i
    if arr[i] == 'KBS2':
        index2 = i

answer += '1'*index1 # KBS1이 있는 곳으로 채널을 내린다
answer += '4'*index1 # KBS1을 1번 채널로 만든다.

if index1 > index2:
    index2 += 1
answer += '1'*index2 # KBS2가 있는 곳으로 채널을 내린다.
answer += '4'*(index2-1)

print(answer)