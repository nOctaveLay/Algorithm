# 신나는 함수 실행
#init
w_list = [[[0]*(21) for _ in range(21)] for _ in range(21)] #init을 할 때 [[0]*n]*n으로 만들면 shallow copy되서 list[0]과 list[1]이 같은 것이 된다!


def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    elif w_list[a][b][c] != 0 : return w_list[a][b][c]
    elif a < b and b < c : w_list[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
    else:
        w_list[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1, b-1, c-1)
    return w_list[a][b][c]

if __name__ == "__main__":   
    import sys
    input = sys.stdin.readline
    while True:
        a,b,c = map(int,input().split())
        if a == -1 and b == -1 and c == -1 : break
        print(f"w({a}, {b}, {c}) = {w(a,b,c)}")