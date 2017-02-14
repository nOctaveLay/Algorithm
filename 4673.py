# 
def self_number(num):
	sum_num = num
	if num >= 10000: 
		sum_num += num //10000
		num %= 10000
	if num >= 1000:
		sum_num += num // 1000
		num %= 1000
	if num >= 100:
		sum_num += num // 100
		num %= 100
	if num >= 10:
		sum_num += num // 10
		num %=10
	sum_num += num
	return sum_num

if __name__ == '__main__':
	result = [0 for _ in range(10000+1)]
	for i in range(1,10000):
		if result[i] != 1: print(i)
		if (self_number(i) < 10000):
			result[self_number(i)] = 1