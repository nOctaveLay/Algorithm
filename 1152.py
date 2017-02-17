in_word = input()
in_word = in_word.split(" ")
if in_word[0] == "":
	in_word.remove(in_word[0])
if in_word[len(in_word)-1] == "":
	in_word.remove(in_word[len(in_word)-1])
print(len(in_word))