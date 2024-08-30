# PYPY로 풀림. python3로는 안 풀림.

import sys
input = sys.stdin.readline

def get_LCS_length(sub1,sub2):
    max_value = 0
    temp = [[0 for _ in range(len(sub2) + 1)] for _ in range(len(sub1)+ 1)]
    for i in range(1, len(sub1)+1):
        for j in range(1, len(sub2)+1):
            if sub1[i-1] == sub2[j-1]:
                temp[i][j] = temp[i-1][j-1] + 1
                max_value = max(max_value, temp[i][j])

    return max_value

if __name__ == "__main__":
    sub1 = input().rstrip("\n")
    sub2 = input().rstrip("\n")
    print(get_LCS_length(sub1, sub2),end='')