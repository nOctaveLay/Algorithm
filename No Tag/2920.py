in_list = input().split(" ")
ascen = ["1","2","3","4","5","6","7","8"]
descen = ["8","7","6","5","4","3","2","1"]
result = ["ascending","descending","mixed"]
if ascen == in_list : print(result[0])
elif descen == in_list : print(result[1])
else:print(result[2])
