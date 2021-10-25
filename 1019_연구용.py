from collections import Counter

def count_numbers(prefix, postfix_len):
    counts = Counter()
    if len(prefix) == 0:
        if postfix_len == 0: return counts
        for i in range(10):
            if i == 0: counts += count_numbers('', postfix_len - 1)
            else: counts += count_numbers(str(i), postfix_len - 1)
        return counts
    for p in prefix:
        counts[int(p)] += 10 ** postfix_len
    if postfix_len > 0:
        for i in range(10):
            counts[i] += postfix_len * (10 ** (postfix_len-1))
    return counts

N = input()
counts = Counter([int(x) for x in N])

for i in range(len(N)):
    for j in range(int(N[i])):
        prefix = N[:i] + ('' if i == 0 and j == 0 else str(j))
        counts += count_numbers(prefix, len(N)-i-1)

print(' '.join(str(counts[x]) for x in range(10)))
