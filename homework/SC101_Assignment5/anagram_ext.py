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


def main():
    """
    To find all anagrams of the input word.
    """
    print(f"Welcome to stanCode \"Anagram Generator\" (or {EXIT} to quit)")
    while True:
        s = input("Find anagrams for: ")
        if s == EXIT:
            break
        start = time.time()
        find_anagrams(s)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.\n')


def find_anagrams(s):
    """
    When reading FILE, if the line of FILE is an anagram of s,
    the program will print out the word.
    :param s: str, the word the user want to search anagrams
    """
    global dictionary
    anagrams = []
    with open(FILE, "r") as f:
        for line in f:
            line = line.strip()
            if len(line) == len(s):
                if compare_vocab(line, s):
                    print("Found:", line)
                    anagrams.append(line)
                    print("Searching...")
        print(f"{len(anagrams)} anagrams: {anagrams}")


def compare_vocab(vocab, s):
    """
    To see if the vocab is an anagram of s, and return boolean.
    :param vocab: str, the line in FILE (ie. all
    vocabs in the dictionary)
    :param s: str, the word the user want to search anagrams
    :return: boolean, True if vocab is an anagram of s
    """
    for ch_s in s:
        stop_delete = False
        tmp = ""
        if ch_s not in vocab:
            return False
        else:
            for ch_vocab in vocab:
                if ch_s == ch_vocab and not stop_delete:
                    stop_delete = True
                elif ch_s != ch_vocab or stop_delete:
                    tmp += ch_vocab
            vocab = tmp
    return True


if __name__ == '__main__':
    main()
