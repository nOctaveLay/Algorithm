while True:
	input_string = input()
	stack = []
	open_backet = ['(','[']
	close_backet = [')', ']']

	if input_string == '.': break

	for x in input_string:
		if x in open_backet:
			stack.append(x)
		if x in close_backet:
			
			if len(stack) == 0:
				stack.append(x)
				break

			a = stack[-1]
			if a == '(' and x == ']' : break
			elif a == '[' and x == ')':break
			stack.pop()

	if len(stack) == 0 : print("yes")
	else: print("no")