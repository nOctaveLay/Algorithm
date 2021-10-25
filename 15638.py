def check_prime(num):
    num = int(num)
    if num < 2: return 0
    i = 2
    while i*i <= num:
        if num % i == 0: return "No"
        i += 1
    return "Yes"

iter_num = int(input())
input_string = input()
string = check_prime(iter_num)
print(string)