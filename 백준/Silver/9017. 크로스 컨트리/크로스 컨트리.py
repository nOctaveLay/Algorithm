import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    n_arr = int(input())
    arr = list(map(int,input().split()))
    team_count = Counter(arr)
    team_score = dict()
    rank = 0
    for i in range(n_arr):
        if team_count[arr[i]] == 6:
            if arr[i] not in team_score:
                team_score[arr[i]] = [rank+1]
            else:
                team_score[arr[i]].append(rank+1)
            rank += 1
    
    # 동점의 경우에는 다섯번째 주자가
    print(sorted(team_score, key = lambda x :(sum(team_score[x][0:4]), team_score[x][4]))[0])
