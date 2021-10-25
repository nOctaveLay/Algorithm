# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def euclid_GCD(input_list):
    # Use a breakpoint in the code line below to debug your script.
    real_a,real_b = input_list
    a = int(real_a)
    b = int(real_b)
    while b != 0:
        n = a%b
        a = b
        b = n
    gcd = a
    lcm = int(real_a) * int(real_b) / gcd
    print(gcd,lcm)

# Press the green button in the gutter to run the script.
input_string = input()
input_list = input_string.split(" ")
euclid_GCD(input_list)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
