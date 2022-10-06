# python에선 stack을 지원하지 않는다 -> deque로 푸는 것이 일반적
from collections import deque

def change_prefix_notation(s):
    answer = ''
    q = deque()
    for c in s:
        if c.isalpha():
            answer += c
        else:
            if c == ')':
                while q and q[-1] != '(': # queue에 원소가 가득차있고, queue에서 (를 만나기 직전 모든 연산자를 다 빼냄
                    answer += q.pop()
                q.pop() # 마지막 (도 없애줌.

            elif c == '*' or c == '/':  # 곱하기, 나누기 뒤엔 곱하기, 나누기가 붙을 수 있음 (우선순위 높음.)
                while q and (q[-1] == '*' or q[-1] =='/'):
                    answer += q.pop()
            
            elif c == '+' or c == '-': # 우선 순위가 낮음 -> 얘가 들어가기 이전에 stack에 연산자가 있었다면 미리 비워둬야함.
                while q and q[-1] != '(':
                    answer += q.pop()

            if c != ')':
                q.append(c) 
    while q:
        answer += q.pop()
    return answer

if __name__ == "__main__":
    s = input().rstrip("\n")

    print(change_prefix_notation(s),end='')