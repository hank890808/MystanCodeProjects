"""
File: coin_flip_runs.py
Name: 蕭承瀚 Hank
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	This program simulates coin flip(s)
	with the number of runs input by users.
	A 'run' is defined as consecutive results
	on either 'H' or 'T'.
	"""
	print("Let's flip a coin!")
	num_run = int(input("Number of runs: "))
	result = ""
	i = 0
	while True:
		if num_run == 0:
			break
		flip = r.randint(0, 1)
		if flip == 0:
			result += "H"
		elif flip == 1:
			result += "T"
		if i == 1:
			if result[i] == result[i-1]:
				num_run -= 1
		elif i > 1:
			if result[i-1] != result[i-2]:
				if result[i] == result[i-1]:
					num_run -= 1
		i += 1
	print(result)


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
