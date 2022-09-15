import sys

# 입력한 정수까지 소수를 찾는다.
# 에라토스테네스의 체를 쓴다.
input_num = int(sys.stdin.readline())

prime_table = [True]*(10**6//2+1) # 2i +1이 소수인지 아닌지를 판별한다.
prime_table[0] = False #i = 0 일경우 (1일 경우) 소수가 아니므로, False

# 에라토스테네스의 체
'''
k*k로 시작하는 이유
1. k = 5라고 가정해보자
2. 그렇다면 k만 남겨두고 5의 배수를 모두 지우니까,  5*2, 5*3, ..., 5*n, ... 이 모두 지워진다.
3. 하지만 5*2, 5*3,5*4 는 이미 2,3 배수를 지울 때 모두 지웠음을 알 수 있다 (즉, 같은 계산을 다시 해 줄 필요가 없다.)
4. 고로 k*k부터 시작해도 무관하다.
5. 2*k로 건너뛰는 이유도 마찬가지. 2의 배수를 모두 지웠기 때문에 2의 배수들은 계산할 필요가 없기 때문이다.
'''
for k in range(3,1000,2): # k하나만 남기고, 나머지 배수들은 모두 지운다.
    if prime_table[k//2] == False: continue
    for x in range(k*k,len(prime_table)*2,2*k):
        prime_table[x//2] = False

for _ in range(input_num):
    n = int(sys.stdin.readline())
    # 출력한다.
    conjecture = 0
    cnt = 0
    for x in range(1,n//2 + 1,2):
        if prime_table[x//2] and prime_table[(n - x)//2]:
            cnt += 1
            conjecture == 1
    if n == 4: cnt += 1
    print(cnt)
