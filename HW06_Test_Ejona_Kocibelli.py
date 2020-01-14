"""
Author: Ejona Kocibelli
Project Description: Testing functions list_copy, list_intersect, list_difference, remove_vowels, check_pwd,
                     and insertion_sort.
"""

import unittest
from HW06_Ejona_Kocibelli import list_copy, list_intersect, list_difference, remove_vowels, check_pwd, insertion_sort


class TestList(unittest.TestCase):
    def test_list_copy(self):
        """ verify that the function returns the copy of the list properly."""
        self.assertEqual(list_copy([1, 2, 3]), [1, 2, 3])
        self.assertEqual(list_copy([]), [])
        self.assertEqual(list_copy([1, ['Ejona', 'Kocibelli'], 2, 'Ejona']), [1, ['Ejona', 'Kocibelli'], 2, 'Ejona'])
        self.assertNotEqual(list_copy(['Ejona', 1, ['Kocibelli']]), ['Ejona', 1, 'Kocibelli'])

    def test_list_intersect(self):
        """ verify that the function returns the intersection of the two lists correctly."""
        self.assertTrue(list_intersect([1, 2, 3], [1, 2, 4]) == [1, 2])
        self.assertTrue(list_intersect([1, 2, 3], [4, 5, 6]) == [])
        self.assertEqual(list_intersect(['Ejona', 'Kocibelli', 1], ['Ejona', 1]), ['Ejona', 1])
        self.assertEqual(list_intersect([], []), [])
        self.assertNotEqual(list_intersect(['Ejona', 'Kocibelli', 1], ['Ejona', 1]), ['Ejona'])

    def test_list_difference(self):
        """ verify that the function returns the new list with values that are in l1 and not in l2."""
        self.assertTrue(list_difference([1, 2, 3], [1, 2, 4]) == [3])
        self.assertTrue(list_difference([1, 2, 3], [4, 5, 6]) == [1, 2, 3])
        self.assertEqual(list_difference([1, 2, 3], [1, 2, 3]), [])
        self.assertEqual(list_difference([], []), [])
        self.assertNotEqual(list_difference([1, 2, 3], [1, 2, 4]), [4])
        self.assertEqual(list_difference(['Ejona', 'Kocibelli', 1], ['Ejona', 1]), ['Kocibelli'])

    def test_remove_vowels(self):
        """ verify that the function returns the string with no vowels in it."""
        self.assertEqual(remove_vowels('hello world'), 'hll wrld')
        self.assertEqual(remove_vowels(''), '')
        self.assertEqual(remove_vowels('EJoNa!234'), 'jn!234')
        self.assertNotEqual(remove_vowels('Ejona1'), 'jna1')
        self.assertEqual(remove_vowels('rbg'), 'rbg')

    def test_check_pwd(self):
        """ verify that the function checks the password and returns True or False properly"""
        self.assertEqual(check_pwd('Ejona1'), True)
        self.assertEqual(check_pwd('ejona1'), False)
        self.assertNotEqual(check_pwd('EJona1'), False)
        self.assertEqual(check_pwd('Ejona'), False)
        self.assertEqual(check_pwd(''), False)

    def test_insertion_sort(self):
        """ verify that the function returns the sorted version of the list properly."""
        self.assertEqual(insertion_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(insertion_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(insertion_sort([]), [])
        self.assertEqual(insertion_sort([5, 2, 1, 4, 3]), [1, 2, 3, 4, 5])
        self.assertNotEqual(insertion_sort([1, 2, 4, 3]), [1, 2, 4, 3])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
