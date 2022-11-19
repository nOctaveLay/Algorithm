from collections import defaultdict
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    result = 0
    '''
    ABCDE 라는 수가 있다면
    A * 10** 4 + B * 10 **3 + C * 10 ** 2 + D * 10 ** 1 + E * 10**0일 것이다.
    그렇다면 A,B,C,D,E를 계수라 하고, 그 뒤에 붙는 숫자들을 자리수라고 한다.
    만약, AAA와 AAB를 더한다고 가정하자, 이는
    A * 10 **2 + A * 10 ** 1 + A * 10 ** 0
    + A * 10 ** 2 + A * 10 ** 1 + B * 10 ** 0
    일 것이다. 
    다시 계수로 묶어쓰면
    A * (2 * 10 ** 2 + 2 * 10 ** 1 + 1) + B * 10 ** 0이 될 것이다.
    즉, 뒤의 자리수들의 합을 알고, A,B를 할당한다면 그 값은 원래 숫자의 합과 같다.
    뒤의 자리수들의 합을 그 수에서 할당된 수치, 즉 할당수치라고 정의하자.
    이 할당수치가 큰 계수에 높은 숫자를 수여한다면, 당연하게도 원래 숫자의 합은 커지게 된다.
    즉 이 문제는 할당수치가 높은 값에 높은 숫자를 부여하면 그것이 답이다.

    '''
    alpha_dict = defaultdict(int) # 계수를 키로 하여 할당수치를 표현한다.
    for _ in range(n):
        num_string = input().rstrip("\n")
        for i, num_char in enumerate(num_string):
            alpha_dict[num_char] += 10 ** (len(num_string) - 1 -i)
    
    # value 순으로 정렬 (할당 숫자가 높은 값으로 정렬)
    alpha_dict = sorted(alpha_dict.items(),key = lambda x:x[1], reverse = True)

    # 할당 숫자가 높은 값에 높은 숫자를 부여
    for i,dicts in enumerate(alpha_dict):
        _,value = dicts
        result += value * (9 - i)

    print(result)
