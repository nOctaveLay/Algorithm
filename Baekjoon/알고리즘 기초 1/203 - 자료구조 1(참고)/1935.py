from collections import deque
import sys

def calculation_prefix(s):
    q = deque()
    for c in s:
        if str(c).isalpha(): q.append(c)
        else:
            if len(q) > 1:
                a, b = q.pop(), q.pop()
                if str(a).isalpha():
                    a = alpha_[a]
                if str(b).isalpha():
                    b = alpha_[b]
                if c == '+' : q.append(a+b)
                elif c == '-' : q.append(b-a)
                elif c == '*' : q.append(a * b)
                else: q.append(round(b/a,2))
    return q.pop()


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    s = input().rstrip("\n")
    alpha_ = dict()
    for i in range(n):
        alpha_[chr(ord('A') + i)] = int(input())
    print(f"{calculation_prefix(s):.2f}") # fstring 주의.