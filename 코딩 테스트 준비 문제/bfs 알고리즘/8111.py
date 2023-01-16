import sys
from collections import deque

def change_num_zero_one(num):
    
    queue = deque([(1, 1)])
    visited = [False for _ in range(num+1)]
    visited[1] = True # 나눠지는지 아닌지는 나머지만 가지고 판단해도 괜찮다.


    while queue:
        modular_num, change_num = queue.popleft()
        if modular_num == 0:
            return change_num

        # 수의 길이를 넘을 조건
        if len(str(num)) > 100:
            return 'BRAK'

        modular_num *= 10
        change_num *= 10
        if not visited[modular_num % num]:
            visited[modular_num % num] = True
            queue.append((modular_num  % num, change_num))

        if not visited[(modular_num  + 1) % num]:
            visited[(modular_num  + 1) % num] = True
            queue.append(((modular_num  + 1) % num, change_num + 1))
    return 'BRAK'

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        print(change_num_zero_one(int(input())))