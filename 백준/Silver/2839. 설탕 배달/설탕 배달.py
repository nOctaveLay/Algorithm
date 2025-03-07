import sys
input=sys.stdin.readline

n=int(input())

# 5로 전부 집을 수 있는 경우
if n%5 == 0:
    print(n//5)

# 5로 전부 집을 수 없는 경우
else:
    q = n // 5
    r = n % 5

    # 3과 5로 이루어져 있는 경우
    # 3 * x + 5 * y인 경우
    # y값이 가질 수 있는 최대한의 정수를 두고 그 나머지가 3으로 나누어 지는 지 확인
    # 계속 반복하여 y == 0일 때 나머지가 3으로 나누어 떨어지지 않는다면 나눠지지 않는 것임
    # 5000 -> 3 * (약)1667 따라서 O(10**6) 보다 작음

    while q:
        if r % 3 == 0:
            print(q + r // 3)
            break
        else:
            q -= 1
            r += 5
    if q == 0 :
        if r % 3 != 0: print(-1)
        else: print(r // 3)