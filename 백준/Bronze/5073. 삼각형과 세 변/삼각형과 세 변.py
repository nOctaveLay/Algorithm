import sys

input = sys.stdin.readline

def check_invalid(a,b,c):
    max_value = 0
    sum_value = 0
    if a >= b and a >= c:
        max_value = a
        sum_value = b+c
    elif b >= c and b >= a:
        max_value = b
        sum_value = a+c
    else:
        max_value = c
        sum_value = a+b

    if max_value < sum_value:
        return False
    else:
        return True

while True:
    a,b,c = map(int,input().split())
    if not (a and b and c): break
    # 삼각형을 만족하지 않는 조건
    if check_invalid(a,b,c):
        print("Invalid")
    
    # 세 변의 길이가 모두 같을 때
    elif a == b and b == c:
        print("Equilateral")

    # 두 변의 길이만 같을 때
    elif a == b or b == c or a == c:
        print("Isosceles")

    # 세 변의 길이가 모두 다를 때
    else:
        print("Scalene")