"""
Author: Ejona Kocibelli
Project Description: Implementing functions anagram_lst, anagrams_dd, anagrams_cntr, covers_alphabet, book_index.
"""
from collections import Counter, defaultdict


def anagram_lst(str1, str2):
    """anagram_lst function returns True if two strings are anagrams, else returns False by using lists"""
    return sorted(str1.upper()) == sorted(str2.upper())


def anagrams_dd(str1, str2):
    """Function anagrams returns True if two string are anagrams, else returns False by using default dictionaries"""
    dd = defaultdict(int)
    for elem in str1.lower():
        dd[elem] += 1
    for c in str2.lower():
        if c in dd:
            dd[c] -= 1
        else:
            return False
    for values in dd.values():
        if values != 0:
            return False
    return True


def anagrams_cntr(str1, str2):
    """anagrams_cntr function returns True if two strings are anagrams, else returns False by using Counter"""
    return Counter(str1.lower()) == Counter(str2.lower())


def covers_alphabet(sentence):
    """covers_alphabet function returns True if the alphabet is a subset of the sentence, else returns False"""
    alphabet = frozenset("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(set(sentence.lower()))


def book_index(word):
    """Function book index returns a list of sorted words with a list of their sorted pages respectively"""
    dd = defaultdict(set)
    for key, value in word:
        dd[key].add(value)
    return sorted([[word, sorted(pages)] for word, pages in dd.items()])
