import sys
input=sys.stdin.readline
n,m=map(int,input().split())
trees=list(map(int,input().split()))
start, end= 1, max(trees)
while start <= end:    
    mid = (start + end) // 2 # 자르기로 결정한 길이의 중간값
    cut_values = sum([i-mid for i in trees if i-mid > 0]) # 나무를 자르고 남은 값들을 전부 더하기
    if cut_values > m:
        start = mid + 1
    elif cut_values < m:
        end = mid - 1
    else:
        print(mid)
        exit()
print(end)