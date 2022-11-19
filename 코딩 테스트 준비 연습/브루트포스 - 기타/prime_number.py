import math


def prime_list(a: int, b: int = -1) -> list[int]:
    """Returns a list of prime numbers in the given range, [1, a] or [a, b]."""
    
    beg, end = (1, a + 1) if b < 0 else (min(a, b), max(a, b) + 1)
    if end < 5:
        return [i for i in range(beg, end) if i in (2, 3)]
    # 2,3 wheel이기 때문에 주기는 6으로 돌아간다.
    period = 2*3

    # 가장 큰 수 wheel을 다 채우기 위해서 행하는 것이다.
    n = (end - end % period) + period

    sieve = [False] + [True] * (n // 3 - 1) # 2의 배수와 3의 배수를 제외한 1 | 3*i + 1이 소수임을 판별하는 체

    # math.isqrt : 음이 아닌 정수 n의 제곱근 반환
    for i in range(math.isqrt(n) // 3 + 1):
        if sieve[i]:
            d, s, j = (k := 1 | 3 * i + 1) * 2, k * k, k * (k + 4 - 2 * (i & 1))
            # 소수가 아닌 애들은 전부 지움.
            sieve[s // 3::d] = [False] * ((n // 6 - s // 6 - 1) // k + 1)
            sieve[j // 3::d] = [False] * ((n // 6 - j // 6 - 1) // k + 1)
    b, e = (beg | 1) // 3, n // 3 - 2 + (end % 6 > 1)
    return ([p for p in (2, 3) if p >= beg] +
            [1 | 3 * i + 1 for i in range(b, e) if sieve[i]])