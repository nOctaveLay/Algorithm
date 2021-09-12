
def euclid_LCM(input_list):
    real_a,real_b = input_list
    a = int(real_a)
    b = int(real_b)
    while b != 0:
        n = a%b
        a = b
        b = n
    gcd = a
    lcm = int(int(real_a) * int(real_b) / gcd)
    print(lcm)

iter_num = int(input())
for _ in range(iter_num):
    input_string = input()
    input_list = input_string.split(" ")
    euclid_LCM(input_list)
