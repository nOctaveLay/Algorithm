import sys

input = sys.stdin.readline

# 최대 값 설정
MAX_N = 10**6

# 홀수 소수 저장 (set 사용)
prime_set = {2}  # 2는 예외적으로 포함
sieve = [True] * ((MAX_N // 2) + 1)

# 에라토스테네스의 체
for i in range(3, int(MAX_N**0.5) + 1, 2):
    if sieve[i // 2]:  # 홀수만 저장됨 (2n+1 구조)
        for j in range(i * i, MAX_N + 1, 2 * i):
            sieve[j // 2] = False

# 소수 집합 생성
prime_set.update(2 * i + 1 for i in range(len(sieve)) if sieve[i])

while True:
    n = int(input().strip())
    if n == 0:
        break

    conjecture = False
    for i in range(3, n // 2 + 1, 2):  # 홀수만 검사
        if (n - i) in prime_set and i in prime_set:
            print(f"{n} = {i} + {n-i}")
            conjecture = True
            break

    if not conjecture:
        print("Goldbach's conjecture is wrong.")