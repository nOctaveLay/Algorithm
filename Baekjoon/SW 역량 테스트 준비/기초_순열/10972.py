# 이 함수는 순열을 list로 받아서 다음 순열을 알려주는 함수이다.
import sys
def next_permutation(input_permutation):
    
    # i, j는 교체할 index를 의미한다.

    i,j = len(input_permutation)-1, len(input_permutation)-1
    
    while i > 0 and input_permutation[i-1] >= input_permutation[i]:
        i -= 1
    
    if i == 0:
        return False

    while j > 0 and input_permutation[i-1] >= input_permutation[j]:
        j -= 1

    input_permutation[i],input_permutation[j] = input_permutation[j],input_permutation[i]

    k = len(input_permutation)-1

    while i < k:
        input_permutation[i],input_permutation[k] = input_permutation[k],input_permutation[i]
        i += 1
        k -= 1
    return input_permutation

max_index = sys.stdin.readline()
input_permutation = sys.stdin.readline().rstrip(" ").split(" ")
print(next_permutation(input_permutation))