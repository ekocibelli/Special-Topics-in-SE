"""
Author: Ejona Kocibelli
Project Description: Implementing and Testing class Fraction, that supports addition, subtraction, multiplication, division and comparison of fractions.
"""
import unittest


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


class Fraction:

    def __init__(self, num, den):
        """ Function __init__ has the parameters that Class Fraction will use: numerator, denominator."""
        self.num = num
        self.den = den
        if den < 0:
            self.num = -1 * self.num
            self.den = -1 * self.den
        if den == 0:
            raise ZeroDivisionError("The denominator can't be zero.")

    def simplify(self):
        common = gcd(self.num, self.den)
        newnum = self.num // common
        newden = self.den // common
        return Fraction(newnum, newden)

    def __add__(self, other):
        """Add fractions"""
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden).simplify()

    def __sub__(self, other):
        """Subtract fractions"""
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden).simplify()

    def __mul__(self, other):
        """Multiply fractions"""
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden).simplify()

    def __truediv__(self, other):
        """Divide fractions"""
        newnum = self.num * other.den
        newden = self.den * other.num
        return Fraction(newnum, newden).simplify()

    def __eq__(self, other):
        """return True/False if the two fractions are equivalent"""
        if self.num * other.den == self.den * other.num:
            return True
        else:
            return False

    def __ne__(self, other):
        """return True/False if the two fractions are not equivalent"""
        if self.num * other.den != self.den * other.num:
            return True
        else:
            return False

    def __lt__(self, other):
        """Compare less than of two fractions, return True/False"""
        if self.num * other.den < self.den * other.num:
            return True
        else:
            return False

    def __le__(self, other):
        """Compare less than or equal of two fractions, return True/False"""
        if self.num * other.den <= self.den * other.num:
            return True
        else:
            return False

    def __gt__(self, other):
        """Compare greater than of two fractions, return True/False"""
        if self.num * other.den > self.den * other.num:
            return True
        else:
            return False

    def __ge__(self, other):
        """Compare greater than or equal of two fractions, return True/False"""
        if self.num * other.den >= self.den * other.num:
            return True
        else:
            return False

    def __str__(self):
        """String to display fractions"""
        return str(self.num) + "/" + str(self.den)


def get_int(prompt):
    """Function get_int makes sure that the user inserts an integer. If the user does not enter an integer,
    the exception catches it and prints a reminder for the user to enter an integer."""
    while True:
        value = input(prompt)
        try:
            i = int(value)
            return i
        except ValueError:
            # Handle the exception
            print("Please enter an integer")


def get_fraction():
    """Function get_fraction gets an input of numerator and denominator from the user. If user input for denominator  is
    0, is an exception and prints a reminder to the user that denominator cannot be zero."""
    while True:
        num = get_int("Enter numerator: ")
        den = get_int("Enter denominator: ")
        try:
            return Fraction(num, den)
        except ZeroDivisionError as e:
            print(e)


def get_operation():
    """Function get_operator gets an input of an operator from the user. If wrong operator prints a reminder to the user
    that the operator he/she chose is wrong. Depending on the operator user chooses, it returns the functions plus/minus
    /divide/times/equal accordingly."""
    f1 = get_fraction()

    while True:
        operation = input("Operation (+,-,*,/,==, !=, <, <=, >, >=): ")
        if operation not in ['+', '-', '*', '/', '==', '!=', '<', '<=', '>', '>=']:
            print("Wrong OPERATION!")
        else:
            break

    f2 = get_fraction()
    if operation == '+':
        return f1 + f2

    elif operation == "-":
        return f1 - f2
    elif operation == "*":
        return f1 * f2
    elif operation == "/":
        return f1 / f2
    elif operation == "==":
        return f1 == f2
    elif operation == "!=":
        return f1 != f2
    elif operation == "<":
        return f1 < f2
    elif operation == "<=":
        return f1 <= f2
    elif operation == ">":
        return f1 > f2
    else:
        return f1 >= f2


class TestFraction(unittest.TestCase):
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

    def test_plus(self):
        """ test fraction addition """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(-1, 3)
        f4 = Fraction(0, 3)
        self.assertTrue((f1 + f1) == Fraction(6, 4))
        self.assertTrue((f1 + f2) == Fraction(5, 4))
        self.assertTrue((f1 + f3) == Fraction(5, 12))
        self.assertTrue(f1 + f2 + f3 == Fraction(11, 12))
        self.assertTrue(f3 + f4 == Fraction(-1, 3))
        self.assertTrue(f3 + f1 == Fraction(5, 12))
        self.assertFalse((f1 + f1) == Fraction(2, 4))

    def test_minus(self):
        """test fraction subtraction"""
        f1 = Fraction(4, 4)
        f2 = Fraction(1, 4)
        f3 = Fraction(-1, 4)
        f4 = Fraction(2, 8)
        self.assertTrue((f1 - f2) == Fraction(3, 4))
        self.assertFalse((f1 - f3) == Fraction(3, 4))
        self.assertTrue((f1 - f3) == Fraction(5, 4))
        self.assertTrue((f2 - f3) == Fraction(2, 4))
        self.assertTrue((f1 - f2 - f3) == Fraction(4, 4))
        self.assertTrue((f1 - f4) == Fraction(6, 8))

    def test_times(self):
        """test fraction multiplication"""
        f1 = Fraction(-4, 4)
        f2 = Fraction(1, -4)
        f3 = Fraction(0, 8)
        f4 = Fraction(1, 2)
        self.assertTrue((f1 * f2) == Fraction(4, 16))
        self.assertTrue((f1 * f1) == Fraction(16, 16))
        self.assertTrue((f1 * f2) == Fraction(-4, -16))
        self.assertTrue((f1 * f3) == Fraction(0, 32))
        self.assertTrue((f2 * f4) == Fraction(1, -8))
        self.assertFalse((f2 * f4) == Fraction(1, 8))

    def test_divide(self):
        """test fraction division"""
        f1 = Fraction(-1, 4)
        f2 = Fraction(-1, 2)
        f3 = Fraction(1, 2)
        self.assertTrue((f1 / f2) == Fraction(2, 4))
        self.assertTrue((f1 / f2) == Fraction(-2, -4))
        self.assertFalse((f1 / f1) == Fraction(4, 16))
        self.assertTrue((f1 / f1) == Fraction(16, 16))
        self.assertTrue((f1 / f2 / f3) == Fraction(-4, -4))
        self.assertTrue((f1 / f2 / f3) == Fraction(4, 4))
        self.assertFalse((f1 / f2 / f3) == Fraction(4, -4))
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

    def test_simplify(self):
        self.assertTrue(str(Fraction(9, 27).simplify()) == "1/3")
        self.assertFalse(str(Fraction(9, 27).simplify()) == str(Fraction(2, 3)))
        self.assertTrue(str(Fraction(-9, -27).simplify()) == str(Fraction(-1, -3)))

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
