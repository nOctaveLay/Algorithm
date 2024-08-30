import sys,itertools
n, m = sys.stdin.readline().rstrip("\n").split(" ")
n, m = int(n), int(m)
iter_product = itertools.product(range(1,n+1),repeat = m)

def check_not_desc(iterable):
    for x in range(len(iterable)-1):
        if iterable[x] > iterable[x+1]:
            return 0
    return 1
    
for product_tuple in iter_product:
    result_string = ''
    if check_not_desc(product_tuple):
        for value in product_tuple[:-1]:
            result_string += f'{value} '
        result_string += f'{product_tuple[-1]}\n'
        sys.stdout.write(f'{result_string}')