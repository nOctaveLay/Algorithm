#9498 test grade
grade = int(input())
if 90 <= grade and grade <= 100:
	print("A")
elif 80 <= grade and grade < 90:
	print("B")
elif 70 <= grade and grade < 80:
	print("C")
elif 60 <= grade and grade < 70:
	print("D")
else:
	print("F")