import sys
input = sys.stdin.readline
'''
1. K보다 작으면서 가장 큰 동전을 집는다.
2. K를 넘지 않는 범위 내에서 최대한 잡는다.
3. 밑의 동전을 잡을 수 있는지 확인한다.
4. 잡지 못하면 그 밑의 동전을 잡을 수 있는지 확인
5. 잡으면 K를 넘지 않는 범위 내에서 최대한 잡는다.

'''

def greedy_pick_up_coin(coin_value_list,K):
    result = 0
    for coin_value in reversed(coin_value_list):
        result += K // coin_value
        K %= coin_value
    return result

if __name__ == "__main__":
    n, k = map(int,input().split())
    coin_value_list = [int(input()) for _ in range(n)]
    sys.stdout.write(str(greedy_pick_up_coin(coin_value_list,k)))