"""
File: anagram.py
Name: Hank 蕭承瀚
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# global
dictionary = []
ans_lst = []


def main():
    """
    To find all anagrams of the input word.
    """
    global ans_lst
    start = time.time()
    ####################
    read_dictionary()
    print(f"Welcome to stanCode \"Anagram Generator\" (or {EXIT} to quit)")
    while True:
        s = input("Find anagrams for: ")
        if s == EXIT:
            break
        find_anagrams(s)
        print(f"{len(ans_lst)} anagrams: {ans_lst}")
        ans_lst = []
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    Read FILE and make the words in it store in dictionary (python list).
    """
    global dictionary
    with open(FILE, "r") as f:
        for line in f:
            dictionary.append(line.strip())


def find_anagrams(s):
    """
    To find all anagrams of s.
    :param s: str, the word the user want to search anagrams
    """
    find_anagrams_helper(s, [])


def find_anagrams_helper(s, current_order_lst):
    """
    First find the permutation of the string order, and then
    rearrange the new word according to the order.
    Print out the word if the new word is in the dictionary.
    :param s: str, the word the user want to search anagrams
    :param current_order_lst: list, the current order when permuting
    """
    if len(current_order_lst) == len(s):
        ans = ""
        for i in range(len(s)):
            ans += s[current_order_lst[i]]
        if ans in dictionary:
            if ans not in ans_lst:
                print(f"Found: {ans}")
                ans_lst.append(ans)
                print("Searching...")
    else:
        for order in range(len(s)):
            if order not in current_order_lst:
                # Choose
                current_order_lst.append(order)
                # Explore
                find_anagrams_helper(s, current_order_lst)
                # Un-choose
                current_order_lst.pop()


if __name__ == '__main__':
    main()
