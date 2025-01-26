import sys
input=sys.stdin.readline

# 100,000 * 3 = 300,000 (3*10**5) -> 1초 안에 가능
n = int(input())
'''
생각
문제의 제한은 4MB = (대략) 4 * 10**3 
파이썬 int 의 크기 = 28bytes
28 * 100000 * 3 = 84 * 100000 = 84* 10**5
모든 배열을 그냥 저장하면 메모리 에러가 뜰 수 밖에 없음.

다음 숫자에서 1번을 선택하려고 할 때 -> 이전 숫자에서 1,2번만 선택 가능
다음 숫자에서 2번을 선택하려고 할 때 -> 이전 숫자에서 1,2,3 모두 선택 가능
다음 숫자에서 3번 선택하려고 할 때 -> 이전 숫자에서 2,3 선택 가능

-> 다음 숫자에 영향을 미치는 것은 이전 숫자밖에 없다. (공통)
-> 이전의 select한 값의 배열만 갖고 있다면 충분하다.
-> 구하려는 것이 max와 min밖에 없으므로, max와 min값만 갖고 있자.
'''
first_input = list(map(int, input().split()))
max_score = first_input[:] # 28 * 3 # max_score[i] = 현 스테이지에서 i번째를 선택했을 경우의 최대값
min_score = first_input[:] # 28 * 3 # min_score[i] = 현 스테이지에서 i번째를 선택했을 경우의 최소값

for _ in range(n-1):
    a1, a2, a3 = map(int,input().split())

    # max값 산출
    current_max1 = a1 + max(max_score[0], max_score[1])
    current_max2 = a2 + max(max_score[0], max_score[1], max_score[2])
    current_max3 = a3 + max(max_score[1], max_score[2])

    # max_score에 대체
    max_score = [current_max1, current_max2, current_max3]

    # min값 산출
    current_min1 = a1 + min(min_score[0], min_score[1])
    current_min2 = a2 + min(min_score[0], min_score[1], min_score[2])
    current_min3 = a3 + min(min_score[1], min_score[2])

    # min_score에 대체
    min_score = [current_min1, current_min2, current_min3]

print(max(max_score), min(min_score))