import sys
# 소수를 구해야되니까 에라토스테네스의 체를 써야겠네
# 간편하게 하면 되지 않아? -> 문제에서 N의 범위가 4,000,000이야...;;
# 그렇다면 sqrt(N) 만큼만 에라토스테네스의 체로 걸러내자
# sqrt(N)...? 그냥 2000까지 구하면 overhead가 너무 심한가?
# 2초니까 너무 심하진 않을거 같은데
def return_sum_prime_table(n):
    prime_table = [True] * ((10**6) * 2 + 1) # 2i + 1이 소수인지 판별.
    prime_table[0] = False

    for k in range(3,2000,2): # 짝수는 prime이 아니기 때문에 제외, (2를 명심할 것.)
        if prime_table[k//2] == False: continue

        # k의 배수들은 모두 지운다.
        for x in range(k*k,len(prime_table)*2,2*k): # 우리는 prime table을 2i + 1이 소수인지 아닌지 판별하는 걸로 하기로 했음.
            prime_table[x//2] = False

    sum_prime_table = [0,2]
    idx = 1
    for i in range(n//2+1):
        if prime_table[i]:
            sum_prime_table.append(sum_prime_table[idx] + i*2+1)
            idx += 1
    return sum_prime_table

def return_num_of_cases_of_sum(m,sum_table):
    s,e = 0,1
    cnt = 0
    n = len(sum_table)
    while s < n:
        prefix_sum = sum_table[e] - sum_table[s]
        if prefix_sum >= m:
            if prefix_sum == m:
                cnt += 1
            s += 1
        elif e == n-1:
            s += 1
        else:
            e += 1
    return cnt

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    sum_table = return_sum_prime_table(n)
    print(return_num_of_cases_of_sum(n,sum_table))