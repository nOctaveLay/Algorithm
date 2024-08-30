# 16936 
# 문제 출처 : https://www.acmicpc.net/problem/16936
# 나3 : x를 3으로 나눈다.
# 곱2 : x에 2를 곱한다. => 즉 2의 배수이다.
import sys
input = sys.stdin.readline

def solution(a:list):
    answer = []
    
    # 소인수 중 3^m에서 m이 가장 큰 수 => 처음 들어갈 수이다.
    # m이 같다면, *2, *4 ... 을 확인해야 하므로 가장 작은 수를 선정해야한다.

    first_pow = 0
    first_num = a[0]
    for a_num in a:
        a_pow = 0
        check_num = a_num
        while check_num % 3 == 0:
            check_num //= 3
            a_pow += 1
        if first_pow < a_pow or (first_pow == a_pow and first_num > a_num):
            first_pow = a_pow
            first_num = a_num
    answer.append(first_num)
    
    for _ in range(len(a)-1):
        if answer[-1] * 2 in a:
            answer.append(answer[-1]*2)
        elif answer[-1] % 3 == 0 and answer[-1] // 3 in a:
            answer.append(answer[-1]//3)
    return answer

if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    result = solution(a)
    print(*result)