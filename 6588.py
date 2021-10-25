import sys

input_num = int(sys.stdin.readline())

# 입력한 정수까지 소수를 찾는다.
# 에라토스테네스의 체를 쓴다.
# 입력한 정수는 6보다 크거나 같다.

prime_table = [True]*(10**6//2+1) # 2i +1이 소수인지 아닌지를 판별한다.
prime_table[0] = False

# 1x 2를 씀, 그리고 2의 배수번째를 False로 만든다.
for k in range(3,1000,2):
    
# n은 이전에 나왔던 수의 배수가 아닐 것.
    if prime_table[k//2] == False: continue
    for x in range(k*k,len(prime_table)*2,2*k):
        prime_table[x//2] = False
 
while True:
    if input_num == 0: break

    # 출력한다.
    conjecture = 0
    for x in range(1,input_num+1,2):
        if prime_table[x//2] != False and prime_table[(input_num - x)//2] != False:
                print(f"{input_num} = {x} + {input_num - x}")
                conjecture = 1
                break

    if conjecture == 0 : print("Goldbach's conjecture is wrong.")
    input_num = int(input(""))