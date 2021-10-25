# 소수를 찾는다. <- 에라토스테네스의 체를 쓴다.
prime_table = [True]*(10**6//2+1) # 2i +1이 소수인지 아닌지를 판별한다.
prime_table[0] = False

# 1x 2를 씀, 그리고 2의 배수번째를 False로 만든다.
for k in range(3,1000,2):

# n은 이전에 나왔던 수의 배수가 아닐 것.
    if prime_table[k//2] == False: continue
    for x in range(k*k,len(prime_table)*2,2*k):
        prime_table[x//2] = False

input_a,input_b = input("").split(" ")
input_a,input_b = int(input_a),int(input_b)
if input_a <= 2 <= input_b : print(2) #a랑 b 사이에 2가 있어야 함
if input_a % 2 == 0 : input_a += 1

# 출력한다.
for x in range(input_a,input_b+1,2):
    if prime_table[x//2] != False:
        print(x)