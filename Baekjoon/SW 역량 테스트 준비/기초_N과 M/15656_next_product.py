import sys,itertools
n, m = sys.stdin.readline().rstrip("\n").split(" ")
n, m = int(n), int(m)
input_list = sys.stdin.readline().rstrip("\n").split(" ")
input_list = sorted([int(x) for x in input_list])
iter_product = itertools.product(input_list,repeat = m)

for product_tuple in iter_product:
    result_string = ''
    for value in product_tuple[:-1]:
        result_string += f'{value} '
    result_string += f'{product_tuple[-1]}\n'
    sys.stdout.write(f'{result_string}')