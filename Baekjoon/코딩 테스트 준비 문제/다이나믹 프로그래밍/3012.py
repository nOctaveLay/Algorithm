
# index [start] 부터 index [end] 까지 올바른 괄호 문자열의 수를 구하는 함수
def get_num_of_right_basket(start, end):
    if start > end: return 1

    # 메모이제이션
    if cache[start][end] != -1: return cache[start][end]

    temp = 0
    for i in range(start + 1, end + 1, 2):
        for k in range(3):
            if arr[start] == open_basket[k] or arr[start] == '?':
                if arr[i] == closed_basket[k] or arr[i] == '?':
                    temp += get_num_of_right_basket(start+1, i-1) * get_num_of_right_basket(i+1, end)

    cache[start][end] = temp
    return temp

if __name__ == "__main__":
    n = int(input())
    arr = input()
    cache = [[-1] * (n+1) for _ in range(n+1)]
    open_basket = "({["
    closed_basket = ")}]"
    result = str(get_num_of_right_basket(0, n-1))
    print(result[-5:])