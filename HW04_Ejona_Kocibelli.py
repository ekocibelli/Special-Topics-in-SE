"""
Author: Ejona Kocibelli
Project Description: Implementing functions count_vowels, last_occurrence, my_enumerate and adding gcd and simplify
function in Fraction class.
"""


def count_vowels(s):
    """Function that counts and returns the number of vowels in a given string"""
    count = 0

    vowels = 'aeiou'
    s = s.lower()
    for letter in s:
        if letter in vowels:
            count += 1
    return count


def last_occurrence(target, string):
    """Function that get's a target character and shows the last occurrence of that character in a given string"""
    for offset, c in enumerate(reversed(string)):
        if c == target:
            return len(string) - 1 - offset
    return None


def my_enumerate(seq):
    """Function that returns an enumerate object. Returns the index and each sequence in that index"""
    yield from zip(range(len(seq)), seq)


def gcd(x, y):
    """greatest common denominator function"""
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
        """Simplifying fractions"""
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