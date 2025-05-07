import sys
input=sys.stdin.readline
n=int(input())

'''
헷갈렸던 점 : 중량이 w인 물체를 들어올린다고 했음
여러 개의 물체를 올려야 하는 것이라 판단했으나, "물체"라고 되어있는 것으로 보아 하나만 들어올리면 됨
예제 입력의 2 10 15 일 때 출력이 20인 것으로 보아 물체들을 들어올리는 것이 아님.
즉 w라고 되어있는 이 물체 하나의 최대치를 물어보는 것임
'''

'''
예제에서, 15kg 밧줄 하나에 매다는 것보다 10kg, 15kg에 20kg 의 물체를 들어올리는 것이 더 이득임
언제나, 밧줄 하나에 매달때엔 가장 최대로 버틸 수 있는 곳에 물체를 다는 게 최대임 (15kg에 15kg를 다는 게 10kg에 10kg 물체를 다는 것보다 더 많이 버틸 수 있음)
밧줄이 늘어날 때마다 더 많은 물체를 달 수 있다면 그것이 최대임 그리고 이것이 항상 보장됨
즉 그리드로 풀 수 있는 문제
'''

arr = sorted([int(input()) for _ in range(n)], reverse=True)

max_weight = arr[0]

for i in range(1,len(arr)):
    weight = arr[i] * (i+1)
    if max_weight < weight:
        max_weight = weight
print(max_weight)

