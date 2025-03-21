import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline

n,m=map(int,input().split())

# 초기 부모 생성
parent=list(i for i in range(n+1))

# a의 최종 부모를 찾기
def find(a): 
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

# a,b를 낮은 숫자를 갖는 같은 부모로 만들기
def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 진실을 아는 사람의 부모를 0으로 통일하기
cnt, *true_list = list(map(int,input().split()))
for true_member in true_list:
    union(0,true_member)

parties = []

for _ in range(m):
    cnt, *party = list(map(int,input().split()))
    parties.append(party)

    # 같은 이야기를 들으면 같은 부모로 (단, 숫자가 낮은 쪽에 맞춤)
    for i in range(cnt-1):
        union(party[i], party[i+1])

cnt = 0
for party in parties:
    if find(party[0]) == 0: # 파티의 멤버 중 한 명이라도 진실을 들었다면
        continue # 그 파티는 검증할 필요가 없음
    
    cnt += 1
print(cnt)