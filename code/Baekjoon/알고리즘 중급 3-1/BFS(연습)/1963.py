import sys
from collections import deque
import math
input = sys.stdin.readline

t = int(input())

# 일단 4자리의 수가 소수인지를 먼저 판별해야 함.
# 에라토스테네스의 체를 쓰면 간단할 거 같은데
# 2i + 1이 소수인지 판별하는 테이블.

max_int = 10001
prime_table = [True for _ in range(max_int//2 + 1)]

def eratos():

    # init : 1은 소수가 아님
    prime_table[0] = False

    # 1보다 큰 수들 중에서, 10001이 만약 합성수라면, 약수의 최대값은 sqrt(10001) 보다 작거나 같은 자연수이다. (1제외)
    # 10001보다 작은 수들은 전부 sqrt(10001)보다 작은 약수들을 갖는다.

    for k in range(3,int(math.sqrt(max_int)),2):

        # n은 이전에 나왔던 수의 배수가 아닐 것.
        # 만약 2k + 1 이 소수가 아니라면, 그 이전에 소수가 아니라고 판별된 것이므로
        # 그 이후의 배수도 소수가 아니다.
        if prime_table[k//2] == False: continue

        # k 보다 작은 배수는 이미 k가 작을 때 처리됬음.
        # k는 홀수여야 되기 때문에, 그리고 k의 배수를 지우는 과정이기 때문에 2k씩 검사해주면 됨.
        for x in range(k*k,max_int,2*k):
            prime_table[x//2] = False

def change_num(num,change_num,digit):
    temp_result = list(str(num))
    temp_result[digit] = change_num
    result = 0
    indices = len(temp_result)-1
    for i in temp_result:
        result += int(i) * (10 ** indices)
        indices -= 1
    return result 

def bfs(start, end):
    q = deque()
    q.append(start)
    distance = [-1 for _ in range(max_int)]
    distance[start-1000] = 0
    while q:
        n = q.popleft()
        if n == end: return distance[end - 1000]
        for i in range(4): # 자리수, 앞부터 변환
            for j in range(10): # 변환.
                next_n = change_num(n,j,i)
                if next_n % 2 != 0 and prime_table[next_n//2]:
                # 다음 이동하려는 숫자가 4자리 수라면, 그리고 방문하지 않았다면
                    if next_n >= 1000 and next_n < 10000 and distance[next_n-1000] == -1 :
                        q.append(next_n)
                        distance[next_n-1000] = distance[n-1000] + 1

for _ in range(t):
    eratos()
    a,b = map(int,input().split())
    print(bfs(a,b))