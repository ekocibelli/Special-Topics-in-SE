"""
Author: Ejona Kocibelli
Project Description: Testing functions anagram_lst, anagrams_dd, anagrams_cntr, covers_alphabet, book_index
"""
import unittest

from HW07_Ejona_Kocibelli import anagram_lst, anagrams_dd, anagrams_cntr, covers_alphabet, book_index


class TestContainer(unittest.TestCase):

    def test_anagram_lst(self):
        """ verify that the function returns True if inputs are anagrams and False otherwise."""
        self.assertEqual(anagram_lst('bay!@', '!yab@'), True)
        self.assertEqual(anagram_lst('', ''), True)
        self.assertEqual(anagram_lst('BAY', 'yab'), True)
        self.assertEqual(anagram_lst('', 's'), False)
        self.assertEqual(anagram_lst('123', '231'), True)
        self.assertEqual(anagram_lst('dormitory', 'dirtyroom'), True)
        self.assertNotEqual(anagram_lst('dormitory', ' dirtyroom '), True)

    def test_anagrams_dd(self):
        """ verify that the function returns True if input are anagrams and False otherwise."""
        self.assertEqual(anagrams_dd('bay!@', '!yab@'), True)
        self.assertEqual(anagrams_dd('', ''), True)
        self.assertEqual(anagrams_dd('BAY', 'yab'), True)
        self.assertEqual(anagrams_dd('', 's'), False)
        self.assertEqual(anagrams_dd('123', '231'), True)
        self.assertEqual(anagrams_dd('Dormitory', 'dirtyroom'), True)
        self.assertNotEqual(anagrams_dd('dormitory', ' dirty room'), True)

    def test_anagrams_cntr(self):
        """ verify that the function returns True if input are anagrams and False otherwise."""
        self.assertEqual(anagrams_cntr('bay!@', '!yab@'), True)
        self.assertEqual(anagrams_cntr('', ''), True)
        self.assertEqual(anagrams_cntr('BAY', 'yab'), True)
        self.assertEqual(anagrams_cntr('', 's'), False)
        self.assertEqual(anagrams_cntr('123', '231'), True)
        self.assertNotEqual(anagrams_cntr('dormitory', 'dirtyroom '), True)

    def test_covers_alphabet(self):
        """ verify that function returns True if the sentence includes the whole alphabet at least once"""
        self.assertEqual(covers_alphabet('the quick brown fox jumps over the lazy dog'), True)
        self.assertEqual(covers_alphabet('aabbcdefghijklmnopqrstuvwxyzzabc'), True)
        self.assertEqual(covers_alphabet('The quick brown fox jumps over the lazy dog'), True)
        self.assertEqual(covers_alphabet('We promptly judged antique ivory buckles for the next prize'), True)
        self.assertEqual(covers_alphabet('The quick, brown, fox; jumps over the lazy dog!'), True)
        self.assertEqual(covers_alphabet('Une jam Ejona Kocibelli'), False)
        self.assertEqual(covers_alphabet(''), False)

    def test_book_index(self):
        """ verify that the function returns a list of sorted words with a list of their sorted pages."""
        input1 = [('how', 3), ('much', 3), ('wood', 3), ('would', 2), ('a', 1), ('woodchuck', 1), ('chuck', 3),
                  ('if', 1), ('a', 1), ('woodchuck', 2), ('could', 2), ('chuck', 1), ('wood', 1)]
        exptect1 = [['a', [1]], ['chuck', [1, 3]], ['could', [2]], ['how', [3]], ['if', [1]], ['much', [3]],
                    ['wood', [1, 3]], ['woodchuck', [1, 2]], ['would', [2]]]

        input2 = [('how', 'three'), ('much', 'three'), ('wood', 'three'), ('would', 'two'), ('a', 'one')]
        expect2 = [['a', ['one']], ['how', ['three']], ['much', ['three']], ['wood', ['three']], ['would', ['two']]]

        input3 = [('word1', 1), ('word2', 2), ('word3', 3), ('word4', 4)]
        expect3 = [['word1', [1]], ['word2', [2]], ['word3', [3]], ['word4', [4]]]

        self.assertEqual(book_index(input1), exptect1)
        self.assertEqual(book_index(input2), expect2)
        self.assertEqual(book_index(input3), expect3)
        self.assertEqual(book_index(([('word', 1)])), [['word', [1]]])
        self.assertEqual(book_index([]), [])
        self.assertNotEqual(book_index(input1), expect2)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
