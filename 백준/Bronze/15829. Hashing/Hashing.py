def h(x):
    """
    x 문자열을 해쉬 변환하는 함수
    Args:
        x (String): input string
    Return:
        result (int): 해쉬 변환된 값
    """
    M =  1234567891
    result = 0
    r0 = 31
    r = 1
    for c in x:
        # 초기 계산
        k = ord(c) - 96
        result += (k * r) % M

        # 반복문 정산
        r *= r0
        r %= M
    return result % M

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n = input()
    x = input().rstrip()
    print(h(x))