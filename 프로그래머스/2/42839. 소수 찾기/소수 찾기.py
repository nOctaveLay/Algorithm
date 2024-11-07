#에라토스테네스의 체를 구현
from itertools import permutations
import math

def check_prime(num):
    if num < 2: return False
    for i in range(2,num//2 + 1):
        if num % i == 0:
            return False
    return True
                        
def solution(numbers):
    # 만들 수 있는 경우의 수를 전부 찾음
    # 2^7 = 128 충분
    answer = 0 
    nums = []
    for r in range(1,len(numbers)+1):
        for num in permutations(numbers, r):
            nums.append(int(''.join(num)))
    for num in set(nums):
        if check_prime(num): 
            answer += 1
    return answer