"""
Author: Ejona Kocibelli
Project Description: Testing functions count_vowels, last_occurrence, my_enumerate and testing simplify and simplified
        adding, subtracting, multiplying and dividing in Fraction class.
"""

import unittest
from HW04_Ejona_Kocibelli import Fraction, count_vowels, last_occurrence, my_enumerate


class FractionTest(unittest.TestCase):

    def test_init(self):
        """ verify that the numerator and denominator are set properly """
        f = Fraction(3, 4)
        self.assertEqual(f.num, 3)
        self.assertEqual(f.den, 4)
        with self.assertRaises(ZeroDivisionError):
            f = Fraction(1, 0)

    def test_str(self):
        """ verify that __str__() works properly """
        f = Fraction(3, 4)
        self.assertEqual(str(f), '3/4')

    def test_simplify(self):
        """verify that simplify() works properly"""
        self.assertTrue(str(Fraction(9, 27).simplify()) == "1/3")
        self.assertFalse(str(Fraction(9, 27).simplify()) == str(Fraction(2, 3)))
        self.assertTrue(str(Fraction(-9, -27).simplify()) == str(Fraction(-1, -3)))
        self.assertTrue(str(Fraction(9, -27).simplify()) == str(Fraction(-1, 3)))

    def test_plus(self):
        """ test fraction addition """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(-1, 4)
        f4 = Fraction(0, 16)
        self.assertTrue((f1 + f1) == Fraction(3, 2))
        self.assertTrue((f1 + f2) == Fraction(5, 4))
        self.assertTrue((f1 + f3) == Fraction(1, 2))
        self.assertTrue(f1 + f2 + f3 == Fraction(1, 1))
        self.assertTrue(f3 + f4 == Fraction(-1, 4))
        self.assertTrue(f3 + f1 == Fraction(1, 2))
        self.assertFalse((f1 + f1) == Fraction(1, 2))

    def test_minus(self):
        """test fraction subtraction"""
        f1 = Fraction(4, 4)
        f2 = Fraction(1, 4)
        f3 = Fraction(-1, 4)
        f4 = Fraction(2, 8)
        self.assertTrue((f1 - f2) == Fraction(3, 4))
        self.assertFalse((f1 - f3) == Fraction(3, 4))
        self.assertTrue((f1 - f3) == Fraction(5, 4))
        self.assertTrue((f2 - f3) == Fraction(1, 2))
        self.assertTrue((f1 - f2 - f3) == Fraction(1, 1))
        self.assertTrue((f1 - f4) == Fraction(3, 4))

    def test_times(self):
        """test fraction multiplication"""
        f1 = Fraction(-4, 4)
        f2 = Fraction(1, -4)
        f3 = Fraction(0, 8)
        f4 = Fraction(1, 2)
        self.assertTrue((f1 * f2) == Fraction(1, 4))
        self.assertTrue((f1 * f1) == Fraction(1, 1))
        self.assertTrue((f1 * f2) == Fraction(-1, -4))
        self.assertTrue((f1 * f3) == Fraction(0, 32))
        self.assertTrue((f2 * f4) == Fraction(1, -8))
        self.assertFalse((f2 * f4) == Fraction(1, 8))

    def test_divide(self):
        """test fraction division"""
        f1 = Fraction(-1, 4)
        f2 = Fraction(-1, 2)
        f3 = Fraction(1, 2)
        self.assertTrue((f1 / f2) == Fraction(1, 2))
        self.assertTrue((f1 / f2) == Fraction(-1, -2))
        self.assertFalse((f1 / f1) == Fraction(1, 4))
        self.assertTrue((f1 / f1) == Fraction(1, 1))
        self.assertTrue((f1 / f2 / f3) == Fraction(-1, -1))
        self.assertTrue((f1 / f2 / f3) == Fraction(1, 1))
        self.assertFalse((f1 / f2 / f3) == Fraction(1, -1))
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 2) / Fraction(0, 3)

    def test_equal(self):
        """test fraction equality"""
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(9, 12)
        f4 = Fraction(-3, -4)
        self.assertTrue(f1 == f1)
        self.assertTrue(f1 == f2)
        self.assertTrue(f1 == f3)
        self.assertTrue(f2 == f3)
        self.assertTrue(f1 == f4 == f2)
        self.assertFalse(f1 == Fraction(3, 5))
        self.assertFalse(f1 == Fraction(-3, 4))

    def test_notequal(self):
        """test fraction not equality"""
        f1 = Fraction(1, 3)
        f2 = Fraction(1, 7)
        f3 = Fraction(-3, -9)
        self.assertFalse(f1 != f1)
        self.assertTrue(f1 != f2)
        self.assertFalse(f1 != f3)
        self.assertTrue(f2 != f3)
        self.assertTrue(f1 != Fraction(-1, 3))
        self.assertFalse(f1 != Fraction(-1, -3))

    def test_lt(self):
        """test fraction less than"""
        f1 = Fraction(1, 3)
        f2 = Fraction(3, 5)
        f3 = Fraction(-3, -9)
        self.assertTrue(f1 < f2)
        self.assertFalse(f1 < f3)
        self.assertFalse(f1 < f1)
        self.assertTrue(f1 < Fraction(-2, -3))

    def test_le(self):
        """test fraction less than or equal"""
        f1 = Fraction(1, 4)
        f2 = Fraction(3, 4)
        f3 = Fraction(-2, -8)
        self.assertTrue(f1 <= f1)
        self.assertTrue(f1 <= f2)
        self.assertTrue(f1 <= f3)
        self.assertTrue(f2 <= f2)
        self.assertFalse(f1 <= Fraction(-1, 4))
        self.assertTrue(f3 <= Fraction(2, 8))
        self.assertFalse(Fraction(-1, 4) <= Fraction(1, -3))

    def test_gt(self):
        """test fraction greater than"""
        f1 = Fraction(1, -4)
        f2 = Fraction(3, 4)
        f3 = Fraction(-2, 8)
        self.assertFalse(f1 > f3)
        self.assertTrue(f2 > f1)
        self.assertTrue(f3 > Fraction(3, -4))

    def test_ge(self):
        """test fraction greater than or equal"""
        f1 = Fraction(1, -4)
        f2 = Fraction(3, 4)
        f3 = Fraction(-2, 8)
        self.assertTrue(f1 >= f1)
        self.assertTrue(f2 >= f1)
        self.assertTrue(f1 >= f3)
        self.assertFalse(f1 >= f2)
        self.assertFalse(f1 >= Fraction(1, 4))

class TestIteration(unittest.TestCase):

    def test_count_vowels(self):
        """test the total number of vowels in a string"""
        self.assertEqual(count_vowels('hello world'), 3)
        self.assertEqual(count_vowels('hEllO world'), 3)
        self.assertNotEqual(count_vowels('hll wrld'), 9)
        self.assertEqual(count_vowels('9876421a!o&g'), 2)
        self.assertEqual(count_vowels('hll wrld'), 0)

    def test_last_occurrence(self):
        """test the last occurrence of an element in a string or list"""
        self.assertEqual(last_occurrence(target='Y', string="pyYthon"), 2)
        self.assertNotEqual(last_occurrence(target='y', string="pyYthon"), 2)
        self.assertEqual(last_occurrence(target='p', string="mississipPi"), 8)
        self.assertEqual(last_occurrence(target='a', string="mississippi"), None)
        self.assertNotEqual(last_occurrence(target='s', string="mississippi"), None)
        self.assertEqual(last_occurrence(target=33, string=[3, 33, 55, 11, 44]), 1)

    def test_my_enumerate(self):
        """test if my_enumerate function and python enumerate function have equal results"""
        self.assertTrue(list(my_enumerate(["ejona"])) == list(enumerate(["ejona"])))
        self.assertFalse(list(my_enumerate(["ejona"])) == list(enumerate(["ejonaejona"])))
        self.assertTrue(list(my_enumerate([3, 33, 11, 44, 67])) == list(enumerate([3, 33, 11, 44, 67])))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
