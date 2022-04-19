"""
File: boggle.py
Name: Hank 蕭承瀚
----------------------------------------
This file simulates a classical board game, Boggle.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	As the user inputs letters, this program will help find
	all words in the 4x4 square grid consists of letters.
	"""
	start = time.time()
	####################
	letters_all = input_letters()
	if letters_all:
		dictionary = read_dictionary()
		word_list = []
		for i in range(4):
			for j in range(4):
				find_word(i, j, letters_all, letters_all[i][j], dictionary, [(i, j)], word_list)
		print(f"There are {len(word_list)} in total.")
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def input_letters():
	"""
	:return letters_all: list, a 4x4 square grid consists of letters
	or [] when the input is illegal
	"""
	letters_all = []
	for i in range(4):
		letters = input(f"{i + 1} row of letters: ")
		letters = letters.split(" ")
		one_row_letter = []
		for letter in letters:
			if len(letter) != 1 or not letter.isalpha():
				print("Illegal input")
				return []
			letter = letter.lower()
			one_row_letter.append(letter)
		letters_all.append(one_row_letter)
	return letters_all


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, "r") as f:
		dictionary = []
		for line in f:
			line = line.strip()
			if len(line) >= 4:
				dictionary.append(line)
	return dictionary


def find_word(i, j, letters_all, current_word, dictionary, index_list, word_list):
	"""
	Find every word in the boggle game.
	:param i: int, the index of letters_all
	:param j: int, the index of letters_all
	:param letters_all: list, letters in a  4x4 square grid
	:param current_word: str, the current word searching in this recursion
	:param dictionary: list, A dictionary contains all words whose length are above 4
	:param index_list: list, consists of which letter in the grid been used
	:param word_list: list, consists of the words been found
	"""
	if not has_prefix(current_word, dictionary):
		if current_word in dictionary:
			print(f"Found \"{current_word}\"")
			word_list.append(current_word)
	else:
		if current_word in dictionary:
			print(f"Found \"{current_word}\"")
			word_list.append(current_word)

		for m in range(-1, 2):
			for n in range(-1, 2):
				if 0 <= i+m < 4 and 0 <= j+n < 4 and (i+m, j+n) not in index_list:
					# Choose
					current_word += letters_all[i+m][j+n]
					index_list.append((i+m, j+n))
					# Explore
					if current_word not in word_list:
						find_word(i+m, j+n, letters_all, current_word, dictionary, index_list, word_list)
					# Un-choose
					tmp = ""
					for x in range(len(current_word)-1):
						tmp += current_word[x]
					current_word = tmp
					index_list.pop()


def has_prefix(sub_s, dictionary):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dictionary: (list) A dictionary contains all words whose length are above 4
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
