# 16637 : https://www.acmicpc.net/problem/16637
# 문제를 꼼꼼히 읽기
from itertools import permutations
import sys

def oper(a:int,b:int,operator:str):
    result = a
    if operator == '+':
        result += b
    elif operator == "-":
        result -= b
    else:
        result *= b
    return result

'''
식은 다음과 같이 구성되어 있다
3 + 8 * 7 - 9 * 2    
즉, 숫자 연산자 숫자 연산자 순이다.

solution의 idx는 괄호를 칠 곳을 나타낸다. (연산자의 위치 -1)
예를 들어, 3+8에 괄호를 치고 싶다고 하자. 그러면 3과 8의 연산을 먼저 한다.
라고 말할 수 있다.
문제의 조건에서, 괄호 안에 연산자가 하나만 들어가 있어야하고, 중첩된 괄호는 사용할 수 없다고 했으므로
괄호는 두 수에만 적용된다. 이 말은 두 수를 먼저 계산한다는 뜻이다.
하나의 수를 연산할 때 idx의 증가량은 2이다 (total + 연산자 숫자)
두개의 수를 연산할 때 idx의 증가량은 4이다. (total + 연산자 (숫자 연산자 숫자))
'''
    
def solution(idx:int, total_sum:int):
    if idx >= n-1: 
        global max_total_sum
        if max_total_sum < total_sum:
            max_total_sum = total_sum
        return

    # 만약 괄호를 치지 않는다면 -> 하나의 수만 계산하고, idx의 증가량은 2이다.
    if idx + 2 < n:
        solution(idx+2,oper(total_sum,int(arr[idx+2]),arr[idx+1]))

    # 만약 괄호를 친다면 -> 괄호를 친 2개의 수를 먼저 계산하고, 그 다음 total과 연산자 계산을 해준다.
    # arr[idx+2], arr[idx+4]
    if idx+4 < n:
        basket = oper(int(arr[idx+2]),int(arr[idx+4]),arr[idx+3])
        solution(idx+4, oper(total_sum,basket,arr[idx+1]))

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = list(input().rstrip("\n"))
    max_total_sum = -200 # 음수도 충분히 나올 수 있다는 점을 감안할것.
    solution(0,int(arr[0]))
    print(max_total_sum)