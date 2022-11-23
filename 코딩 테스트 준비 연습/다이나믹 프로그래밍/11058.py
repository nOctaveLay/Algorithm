import sys
input = sys.stdin.readline

def get_num_of_a(n:int)->int:

    # 초기화 : print('A')만 했을 경우 A의 갯수
    dp = [i for i in range(n+1)]

    # ctrl + v를 하는 횟수에 따라 dp 갱신
    # ctrl + v를 하기 전에 ctrl + A, ctrl + C를 한다.
    # ctrl + c, ctrl + v를 하기 위해선 이미 출력창에 'A'문자가 적어도 하나는 존재해야 한다.
    # 따라서 dp의 갱신 범위는 4부터 진행된다.

    for i in range(4,n+1):
        for j in range(i-2): # print a, ctrl+c, ctrl+v를 할 수 있는 최소 한도.
            dp[i] = max(dp[i-2-j]*(1+j), dp[i])
    return dp[n]

if __name__ == "__main__":
    n = int(input())
    print(get_num_of_a(n))