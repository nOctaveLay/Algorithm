import sys

input = sys.stdin.readline

n, t_score, p = map(int,input().split())

# 같을 때 처리하는 게 생각보다 빡세다.
a = sorted(list(map(int,input().split())),reverse=True) if n > 0 else []

def find_rank(a):
    if len(a) == 0: return 1
    end_a = len(a) if len(a) < p else p
    for i in range(end_a):
        if a[i] < t_score:
            return i+1
        elif a[i] == t_score:
            for j in range(i, end_a):
                if a[j] != t_score:
                    return i+1
            if len(a) < p:
                return i + 1
            return -1

    if len(a) < p:
        return len(a) + 1
    else:
        return -1

print(find_rank(a))