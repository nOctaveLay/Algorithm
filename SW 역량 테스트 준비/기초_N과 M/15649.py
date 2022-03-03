#아무리봐도 next_permutation 구현하는 것임.
import sys,itertools
n, m = sys.stdin.readline().rstrip("\n").split(" ")
n, m = int(n), int(m)
iter_permutation = itertools.permutations(range(1,n+1),m)
for permutation_tuple in iter_permutation:
    result_string = ''
    
    for value in permutation_tuple:
        if value != permutation_tuple[-1]:
            result_string += f'{value} '
        else:
            result_string += f'{value}'
    sys.stdout.write(f'{result_string}\n')