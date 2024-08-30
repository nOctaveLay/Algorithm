import sys

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

	
if __name__ == "__main__":
    input = sys.stdin.readline
    num = input().rstrip("\n")
    while (num != '0'):
        combination_list = list(map(int,num.split(" ")))
        iter_combinations = combinations(combination_list[1:],6)
        for combination_elem in iter_combinations:
            print(*combination_elem,sep=' ',end='\n')
        print()
        num = input().rstrip("\n")