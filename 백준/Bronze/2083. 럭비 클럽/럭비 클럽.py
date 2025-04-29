import sys

input=sys.stdin.readline

while True:
    
    input_string = input().rstrip()
    if input_string == "# 0 0":
        break
    else:
        name, age, weight = input_string.split()
        age, weight = int(age), int(weight)

        if age > 17 or weight >=80:
            print(name, "Senior")
        else:
            print(name, "Junior")

