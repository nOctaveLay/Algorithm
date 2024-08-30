import sys
iter_n = int(sys.stdin.readline())

fn_table = [1]*(10**6+1) #f(n)값을 가지고 있는 table
gn_table = [1]*(10**6+1) #g(n)값을 가지고 있는 table
gn_table[0] = 0

# 나는 이 문제를 에라토스테네스의 체와 유사하다고 생각하여, 에라토스테네스의 체를 쓰기로 했다.
# fn_table: fn_table[n] = f(n)의 값이다.
# f(n)은 약수들의 합이다.
# i가 n의 약수라는 말은 n = i*j (단, k는 자연수)를 만족한다는 뜻이다.
# 즉, n이 i의 배수라면 i는 n의 약수라고 말할 수 있을 것이다.
# 따라서 i의 배수가 된다면, i는 그 수의 약수라고 말할 수 있을 것이다.
# 즉, f(n)은 약수들의 합이므로, f(n) += i를 해주면 된다.

for i in range(2,10**6 + 1):
    j = 1
    while i * j < (10**6 + 1):
        fn_table[i*j] += i
        j += 1

for i in range(1,10**6+1):
    gn_table[i] = gn_table[i-1] + fn_table[i]
    
for _ in range(iter_n):
    n = int(sys.stdin.readline())
    print(gn_table[n])