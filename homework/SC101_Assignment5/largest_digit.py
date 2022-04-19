"""
File: largest_digit.py
Name: Hank 蕭承瀚
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	To find the largest digit of n.
	:param n: int, the origin number
	:return: int, the largest digit
	"""
	if n < 0:
		n *= -1
	return find_largest_digit_helper(n, 0)


def find_largest_digit_helper(n, current_largest):
	"""
	Find units digit of n, and see if the digit is larger than current_largest,
	and then remove the units digit.
	:param n: int/float
	:param current_largest: int/float, the current largest number
	:return base: int, the largest digit
	:return recursive: function, find_largest_digit_helper() as recursive function
	"""
	if n == 0:
		return int(current_largest)
	else:
		tmp = n % 10
		n = (n-tmp)/10
		if tmp > current_largest:
			current_largest = tmp
		return find_largest_digit_helper(n, current_largest)


if __name__ == '__main__':
	main()
