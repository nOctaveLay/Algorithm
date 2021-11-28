import sys,itertools

n, m = sys.stdin.readline().rstrip("\n").split(" ")
n, m = int(n), int(m)
input_list = sys.stdin.readline().rstrip("\n").split(" ")
input_list = [int(x) for x in input_list]
input_list = sorted(input_list)
iter_permutation = itertools.permutations(input_list,m)

def check_asc(iterable):
    for x in range(len(iterable)-1):
        if iterable[x] > iterable[x+1]:
            return 0
    return 1

for permutation_tuple in iter_permutation:
    result_string = ''
    if check_asc(permutation_tuple):
        for value in permutation_tuple:
            if value != permutation_tuple[-1]:
                result_string += f'{value} '
            else:
                result_string += f'{value}'
        sys.stdout.write(f'{result_string}\n')