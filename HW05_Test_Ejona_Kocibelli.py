"""
Author: Ejona Kocibelli
Project Description: Testing functions reverse, rev_enumerate, find_second, get_lines.
"""

import unittest
from HW05_Ejona_Kocibelli import reverse, rev_enumerate, find_second, get_lines


class TestString(unittest.TestCase):
    def test_reverse(self):
        """ verify that the function reverses the strings properly."""
        self.assertEqual((reverse("ALBI AND EJONA")), "ANOJE DNA IBLA")
        self.assertEqual(reverse("Hello"), "olleH")
        self.assertEqual(reverse(""), "")

    def test_rev_enumerate(self):
        """ verify that the function reverses the sequence and the offset correctly."""
        expected = [(4, 'a'), (3, 'n'), (2, 'o'), (1, 'j'), (0, 'e')]
        result = list(rev_enumerate("ejona"))
        self.assertEqual(list(rev_enumerate("ejona")), list(reversed(list(enumerate("ejona")))))
        self.assertEqual(list(rev_enumerate([3, 33, 11, 44, 67])),
                         list(reversed(list(enumerate([3, 33, 11, 44, 67])))))
        self.assertNotEqual(list(rev_enumerate(["ejona"])), list(reversed(list(enumerate("ejonaejona")))))
        self.assertEqual(list(rev_enumerate("")), list(reversed(list(enumerate("")))))
        self.assertEqual(result, expected)

    def test_find_second(self):
        """ verify that the function the second appearance of a substring in a string properly."""
        self.assertTrue(find_second('iss', 'Mississippi') == 4)
        self.assertTrue(find_second('abba', 'abbabba') == 3)
        self.assertTrue(find_second('ab', 'Eabjona') == -1)
        self.assertTrue(find_second('ab', 'Ejona') == -1)
        self.assertTrue(find_second('ab', 'abEjonabjab') == 6)

    def test_get_lines(self):
        """ verify that the function reads and yields the information of the file properly"""
        self.file_path = 'text.txt'
        expect = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>', '<line4.1 line4.2>', '<line5>',
                  '<line6>']
        result = list(get_lines('text.txt'))
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
