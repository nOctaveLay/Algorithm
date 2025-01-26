import sys
input=sys.stdin.readline
# 설명 없는 버전. -> 설명 이전 버전 참고

n = int(input())

first_input = list(map(int, input().split()))
max_score = first_input[:] 
min_score = first_input[:] 

for _ in range(n-1):
    a1, a2, a3 = map(int,input().split())
    max_score = [a1 + max(max_score[0], max_score[1]), a2 + max(max_score[0], max_score[1], max_score[2]), a3 + max(max_score[1], max_score[2])]
    min_score = [a1 + min(min_score[0], min_score[1]),a2 + min(min_score[0], min_score[1], min_score[2]), a3 + min(min_score[1], min_score[2])]

print(max(max_score), min(min_score))