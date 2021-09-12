def check_prime(num):
    num = int(num)
    if num < 2: return 0
    i = 2
    while i*i <= num:
        if num % i == 0: return 0
        i += 1
    return 1

iter_num = int(input())
input_string = input()
prime_set = input_string.split(" ")
sum = 0
for prime_num in prime_set:
    sum += check_prime(prime_num)
print(sum)
