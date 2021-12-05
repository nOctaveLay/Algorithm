input_string = input()
while(input_string != "."):
	stack = []
	for x in input_string:
		if x == '(' or x == '[':
			stack.append(x)
			# print(stack)
		if x == ')' or x == ']':
			if len(stack) == 0: 
				stack.append(x)
				break
			a = stack.pop()
			if a == '(' and x == ']' : 
				stack.append(a) 
				break
			elif a == '[' and x == ')': 
				stack.append(a)
				break
	if len(stack) == 0 : print("yes")
	else: print("no")
	input_string = input()
