while True:
	input_string = input()
	stack = []
	open_backet = ['(','[']
	close_backet = [')', ']']

	if input_string == '.': break

	for elem in input_string:
		if elem in open_backet: stack.append(elem)

		if elem in close_backet:
			if len(stack) == 0: stack.append(elem); break;
			
			check_open = stack[-1]
			if check_open == '(' and elem == ']' : break
			elif check_open == '[' and elem == ')':break
			else: stack.pop()

	print("yes" if len(stack) == 0 else "no")