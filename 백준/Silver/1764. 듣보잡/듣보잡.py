# list의 in 연산은 O(n) 이지만, set의 in 연산은 O(1)이다.
import sys
input = sys.stdin.readline
n,m=map(int,input().split())
not_hear_people = set(input().rstrip() for _ in range(n))
result = list()
for _ in range(m):
    not_seen_person = input().rstrip()
    
    if not_seen_person in not_hear_people:
        result.append(not_seen_person)
print(len(result))
result.sort()
print(*result, sep='\n')